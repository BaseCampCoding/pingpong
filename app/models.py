from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError

USER_MODEL = get_user_model()


class Game(models.Model):
    player_1 = models.ForeignKey(
        USER_MODEL,
        related_name='player_1_games',
        on_delete=models.PROTECT,
    )
    player_2 = models.ForeignKey(
        USER_MODEL,
        related_name='player_2_games',
        on_delete=models.PROTECT,
    )
    points = ArrayField(models.IntegerField(), default=list)

    def clean(self):
        super().clean()
        self.ensure_all_points_for_games_players()

    def ensure_all_points_for_games_players(self):
        for point, winner in enumerate(self.points, 1):
            if winner not in [self.player_1.id, self.player_2.id]:
                raise ValidationError(
                    f'Invalid Point #{point} winner :{winner}')

    @property
    def game_finished(self):
        return self.players_score(self.player_1) == 10 or \
               self.players_score(self.player_2) == 10

    @property
    def winner(self):
        if not self.game_finished:
            return None
        else:
            return max([self.player_1, self.player_2], key=self.players_score)

    @property
    def loser(self):
        if not self.game_finished:
            return None
        else:
            return min([self.player_1, self.player_2], key=self.players_score)

    @property
    def winner_score(self):
        return self.players_score(self.winner)

    @property
    def loser_score(self):
        return self.players_score(self.loser)

    def players_score(self, player):
        return sum(winner == player.id for winner in self.points)
