from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
USER_MODEL = get_user_model()


class TestApiCanLogin(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = USER_MODEL.objects.create(username='natec425')
        cls.user.set_password('testpass')
        cls.user.save()

    def test_submitting_valid_data_returns_a_token(self):
        response = self.client.post(
            reverse('api:login'),
            data={
                'username': 'natec425',
                'password': 'testpass',
            },
            format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.data,
        )
        self.assertIn('token', response.data)

    def test_not_submitting_all_the_data_errors(self):
        response = self.client.post(
            reverse('api:login'),
            data={},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_submitting_invalid_password_responds_with_error(self):
        response = self.client.post(
            reverse('api:login'),
            data={
                'username': 'natec425',
                'password': 'badpass'
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
