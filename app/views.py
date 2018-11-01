from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView, CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model

from .forms import RegistrationForm, GameUpdateForm
from . import models


class RegistrationView(CreateView):
    model = get_user_model()
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('app:user-home')


class UserHome(TemplateView):
    template_name = 'registration.html'


class Login(LoginView):
    template_name = 'login.html'


class NewGame(CreateView):
    model = models.Game
    template_name = 'new-game.html'
    fields = ['player_1', 'player_2']

    def get_success_url(self):
        return reverse('app:score-game', kwargs={'id': self.object.id})


class Game(DetailView):
    context_object_name = 'game'
    model = models.Game
    pk_url_kwarg = 'id'
    template_name = 'game.html'


class ScoreGame(UpdateView):
    model = models.Game
    pk_url_kwarg = 'id'
    template_name = 'score-game.html'
    form_class = GameUpdateForm

    def get_success_url(self):
        return reverse('app:game', kwargs={'id': self.object.id})


registration = RegistrationView.as_view()
user_home = UserHome.as_view()
login = Login.as_view()
new_game = NewGame.as_view()
game = Game.as_view()
score_game = ScoreGame.as_view()
