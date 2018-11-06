from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model
from contextlib import contextmanager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.expected_conditions import staleness_of

from django.urls import reverse, resolve, Resolver404
from urllib.parse import urlparse


class SeleniumTestCase(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Chrome(options=options)
        self.browser.implicitly_wait(2)

        self.setUpTestData()

    def setUpTestData(self):
        pass

    def tearDown(self):
        self.browser.quit()

    def visit(self, *args, **kwargs):
        self.browser.get(self.live_server_url + reverse(*args, **kwargs))

    def fill_out(self, form_name: str, values: dict, *, submit: bool):
        try:
            form = self.browser.find_element_by_name(form_name)
        except NoSuchElementException:
            html = self.browser.find_element_by_tag_name('body').text
            raise AssertionError(
                f'Unable to find form {form_name} in page:\n{html}', )
        for input_name, value in values.items():
            form.find_element_by_name(input_name).send_keys(value)
        if submit:
            form.submit()

    @property
    def current_path(self):
        return urlparse(self.browser.current_url).path

    @property
    def current_view(self):
        try:
            return resolve(self.current_path).view_name
        except Resolver404:
            return None

    @property
    def current_text(self):
        return self.browser.find_element_by_tag_name('body').text

    @contextmanager
    def wait_for_page_load(self, timeout=2):
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(staleness_of(old_page))

    def assert_current_view(self, view_name):
        old_page = self.browser.find_element_by_tag_name('html')
        if self.current_view != view_name:
            try:
                WebDriverWait(self.browser, 2).until(staleness_of(old_page))
            except TimeoutException:
                raise AssertionError(
                    f'Expected view {view_name} != current view {self.current_view}'
                )
        self.assertEqual(self.current_view, view_name, self.current_text)

    def create_user(self, *, username, password):
        model = get_user_model()
        user = model.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        return user

    def assertElementExists(self, selector, text=None):
        try:
            element = self.browser.find_element_by_css_selector(selector)
        except NoSuchElementException:
            raise AssertionError(f'Unable to find element {selector}')
        else:
            if text is not None and text not in element.text:
                raise AssertionError(
                    f'Element {selector} didn\'t contain "{text}"\n'
                    f'Instead it contained the the following text:\n{element.text}'
                )
