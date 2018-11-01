from django.test import SimpleTestCase
from ..models import Game
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

USER_MODEL = get_user_model()


class GameTestCase(SimpleTestCase):
    player_1 = USER_MODEL(id=1)
    player_2 = USER_MODEL(id=2)

    def new_game(self, *, player_1_points, player_2_points):
        return Game(
            player_1=self.player_1,
            player_2=self.player_2,
            points=[self.player_1.id for _ in range(player_1_points)] + \
                   [self.player_2.id for _ in range(player_2_points)],
        )


class TestGameIsFinished(GameTestCase):
    def test_if_player_1_has_ten_points(self):
        game = self.new_game(player_1_points=10, player_2_points=0)
        self.assertTrue(game.game_finished)

    def test_if_player_two_has_ten_points(self):
        game = self.new_game(player_1_points=0, player_2_points=10)
        self.assertTrue(game.game_finished)

    def test_if_player_one_wins_10_to_9(self):
        game = self.new_game(player_1_points=10, player_2_points=9)
        self.assertTrue(game.game_finished)


class TestGameIsNotFinished(GameTestCase):
    def test_if_no_one_has_scored(self):
        game = self.new_game(player_1_points=0, player_2_points=0)
        self.assertFalse(game.game_finished)

    def test_if_the_game_is_tied_5_to_5(self):
        game = self.new_game(player_1_points=5, player_2_points=2)
        self.assertFalse(game.game_finished)

    def test_if_the_game_is_tied_9_to_9(self):
        game = self.new_game(player_1_points=9, player_2_points=9)
        self.assertFalse(game.game_finished)


class TestGameIsInvalid(GameTestCase):
    def test_if_an_unrelated_player_has_a_point(self):
        game = Game(
            player_1=self.player_1,
            player_2=self.player_2,
            points=[123456],
        )

        with self.assertRaisesMessage(ValidationError,
                                      'Invalid Point #1 winner :123456'):
            game.clean()

    def test_if_player_1_has_more_than_10_points(self):
        game = self.new_game(player_1_points=11, player_2_points=0)

        with self.assertRaisesMessage(
                ValidationError,
                'Invalid Score: Player 1 has more than 10 points'):
            game.clean()

    def test_if_player_2_has_more_than_10_points(self):
        game = self.new_game(player_1_points=0, player_2_points=11)

        with self.assertRaisesMessage(
                ValidationError,
                'Invalid Score: Player 2 has more than 10 points'):
            game.clean()
