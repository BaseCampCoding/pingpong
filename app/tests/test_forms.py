from django.test import SimpleTestCase
from .. import forms


class RegistrationTest(SimpleTestCase):
    username = 'natec425'
    password = 'GoodPassword!123'

    def test_matching_passwords_are_valid(self):
        form = forms.RegistrationForm({
            'username': self.username,
            'password': self.password,
            'password_repeat': self.password,
        })

        self.assertTrue(form.is_valid())

    def test_non_matching_passwords_is_invalid(self):
        form = forms.RegistrationForm({
            'username': self.username,
            'password': self.password,
            'password_repeat': self.password + '!'
        })

        self.assertFalse(form.is_valid())
