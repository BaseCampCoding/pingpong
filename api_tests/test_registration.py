from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestApiCanCreateANewUser(APITestCase):
    def test_submitting_valid_data_returns_a_token(self):
        response = self.client.post(
            reverse('api:login'),
            data={
                'username': 'natec425',
                'password': 'GoodPassword123!',
                'passwordRepeat': 'GoodPassword123!'
            },
            format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_not_submitting_all_the_data_returns_an_error(self):
        response = self.client.post(
            reverse('api:login'),
            data={},
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', response.data)
        self.assertNotIn('token', response.data)
