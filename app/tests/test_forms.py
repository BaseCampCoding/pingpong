from django.test import TestCase, SimpleTestCase
from .. import forms


class RegistrationTest(TestCase):
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


class TestGameUpdateFormCoalescesPointsCorrectly(SimpleTestCase):
    def test_user_1_wins_10_0(self):
        points = forms.GameUpdateForm.point_fields_to_list({
            'point_1': 1,
            'point_2': 1,
            'point_3': 1,
            'point_4': 1,
            'point_5': 1,
            'point_6': 1,
            'point_7': 1,
            'point_8': 1,
            'point_9': 1,
            'point_10': 1,
        })

        self.assertListEqual([1 for _ in range(10)], points)

    def test_users_trade_3_points_back_and_forth(self):
        points = forms.GameUpdateForm.point_fields_to_list({
            'point_1': 1,
            'point_2': 1,
            'point_3': 1,
            'point_4': 2,
            'point_5': 2,
            'point_6': 2,
            'point_7': 1,
            'point_8': 1,
            'point_9': 1,
            'point_10': 2,
            'point_11': 2,
            'point_12': 2,
            'point_13': 1,
            'point_14': 1,
            'point_15': 1,
            'point_16': 2,
            'point_17': 2,
            'point_18': 2,
            'point_19': 1
        })

        self.assertListEqual(
            [1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1], points)

    def test_ignores_points_winless_points(self):
        points = forms.GameUpdateForm.point_fields_to_list({
            'point_1': 1,
            'point_2': 1,
            'point_3': 1,
            'point_4': 1,
            'point_5': 1,
            'point_6': 1,
            'point_7': 1,
            'point_8': 1,
            'point_9': 1,
            'point_10': 1,
            'point_11': None,
            'point_12': None
        })

        self.assertListEqual([1 for _ in range(10)], points)
