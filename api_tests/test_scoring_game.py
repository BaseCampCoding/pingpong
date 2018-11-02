from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from app.models import Game

User = get_user_model()


class TestAPICanScoreAGame(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.nate = User.objects.create(username='nate', password='testpass')
        cls.nate_token = Token.objects.create(user=cls.nate)
        cls.player1 = User.objects.create(
            username='player1', password='testpass')
        cls.player2 = User.objects.create(
            username='player2', password='testpass')
        cls.game = Game.objects.create(
            referee=cls.nate,
            player_1=cls.player1,
            player_2=cls.player2,
            points=[],
        )

    def test_nate_watches_player_1_skunk_player_2(self):
        response = self.client.patch(
            reverse('api:score-game', kwargs={'id': self.game.id}),
            data={'points': [self.player1.id for _ in range(10)]},
            format='json',
            HTTP_AUTHORIZATION=f'Token {self.nate_token}')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.data,
        )

        self.assertDictContainsSubset(
            {
                'id': self.game.id,
                'points': [self.player1.id for _ in range(10)],
                'player_1': self.player1.id,
                'player_2': self.player2.id,
                'referee': self.nate.id,
                'winner': self.player1.id,
                'loser': self.player2.id
            }, response.data)
