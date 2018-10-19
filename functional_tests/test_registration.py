from functional_tests import SeleniumTestCase


class RegistrationTest(SeleniumTestCase):
    username = 'natec425'
    password = 'SuperGoodPassword!123'

    def test_user_can_create_a_new_account(self):
        self.visit_registration_page()
        self.fill_out_registration_form()
        self.should_be_on_user_homepage()

    def visit_registration_page(self):
        self.visit('app:registration')

    def fill_out_registration_form(self):
        self.fill_out(
            'registration-form', {
                'username': self.username,
                'password': self.password,
                'password-repeat': self.password
            },
            submit=True)

    def should_be_on_user_homepage(self):
        assert self.current_view == 'app:user:home'
