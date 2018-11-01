from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class TestAPICanRegisterANewUser(APITestCase):
    def test_submitting_valid_data_returns_a_token(self):
        response = self.client.post(
            reverse('api:register'),
            data={
                'username': 'natec425',
                'password': 'testpass',
                'password_repeat': 'testpass'
            },
            format='json')

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            response.data,
        )
        self.assertIn('token', response.data)
        self.assertTrue(
            USER_MODEL.objects.filter(username='natec425').exists())

    def test_not_submitting_all_the_data_errors(self):
        response = self.client.post(
            reverse('api:register'),
            data={},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)

    def test_submitting_invalid_password_responds_with_error(self):
        response = self.client.post(
            reverse('api:register'),
            data={
                'username': 'natec425',
                'password': 'badpass'
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
