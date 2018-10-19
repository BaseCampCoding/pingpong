from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from django.urls import reverse, resolve, Resolver404
from urllib.parse import urlparse


class SeleniumTestCase(LiveServerTestCase):
    def setUp(self):
        firefox_options = Options()
        firefox_options.headless = True
        self.browser = webdriver.Firefox(firefox_options=firefox_options)

    def tearDown(self):
        self.browser.quit()

    def visit(self, *args, **kwargs):
        self.browser.get(reverse(*args, **kwargs))

    def fill_out(self, form_name: str, values: dict, *, submit: bool):
        form = self.browser.find_element_by_name(form_name)
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
