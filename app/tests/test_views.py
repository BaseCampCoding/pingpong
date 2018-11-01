from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth import get_user_model
from .. import views, models


class RegistrationTest(TestCase):
    def setUp(self):
        self.UserModel = get_user_model()

    def test_creates_a_user(self):
        self.client.post(
            reverse('app:registration'),
            data={
                'username': 'natec425',
                'password': 'GoodPassword123!',
                'password_repeat': 'GoodPassword123!',
            })

        self.assertTrue(
            self.UserModel.objects.filter(username='natec425').exists())


class ScoreGameTest(TestCase):
    def setUp(self):
        self.UserModel = get_user_model()
        self.nate = self.UserModel.objects.create_user(
            username='nate', password='testpass')
        self.megan = self.UserModel.objects.create_user(
            username='megan', password='testpass')
        self.game = models.Game.objects.create(
            player_1=self.nate,
            player_2=self.megan,
        )

    def test_nate_can_win(self):
        request = self.client.post(
            reverse('app:score-game', kwargs={'id': self.game.id}),
            data={
                f'point_{which_point}': self.nate.id
                for which_point in range(1, 11)
            })
