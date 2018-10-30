from functional_tests import SeleniumTestCase


class LoginTest(SeleniumTestCase):
    username = 'natec425'
    password = 'Goodpassword!123'

    def setUpTestData(self):
        self.create_user(username=self.username, password=self.password)

    def test_existing_user_can_login(self):
        self.go_to_login_page()
        self.fill_out_login_form()
        self.should_be_on_user_homepage()

    def go_to_login_page(self):
        self.visit('app:login')

    def fill_out_login_form(self):
        self.fill_out(
            'login-form',
            {
                'username': self.username,
                'password': self.password,
            },
            submit=True,
        )

    def should_be_on_user_homepage(self):
        self.assert_current_view('app:user-home')
