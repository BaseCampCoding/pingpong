from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth import get_user_model
from .. import views


class RegistrationTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.UserModel = get_user_model()

    def test_creates_a_user(self):
        request = self.factory.post(
            reverse('app:registration'),
            data={
                'username': 'natec425',
                'password': 'GoodPassword123!',
                'password_repeat': 'GoodPassword123!',
            })

        views.registration(request)

        self.assertTrue(
            self.UserModel.objects.filter(username='natec425').exists())
