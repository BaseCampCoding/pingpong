from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class TestAPICanCreateANewGame(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.nate = User.objects.create(username='nate', password='testpass')
        cls.nate_token = Token.objects.create(user=cls.nate)
        cls.player1 = User.objects.create(
            username='player1', password='testpass')
        cls.player2 = User.objects.create(
            username='player2', password='testpass')

    def test_nate_referees_for_two_players(self):
        response = self.client.post(
            reverse('api:new-game'),
            data={
                'player_1': self.player1.id,
                'player_2': self.player2.id
            },
            format='json',
            HTTP_AUTHORIZATION=f'Token {self.nate_token}')

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            response.data,
        )
        self.assertDictContainsSubset({
            'points': [],
            'player_1': self.player1.id,
            'player_2': self.player2.id,
            'referee': self.nate.id
        }, response.data)
        self.assertIn('id', response.data)
