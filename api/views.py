from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from app.models import Game
from rest_framework.permissions import IsAuthenticated

from .serializers import UserCreationSerializer, GameCreationSerializer, ScoreGameSerializer
from .permissions import IsReferee

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer


class GameCreationView(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(referee=self.request.user, points=[])


class ScoreGameView(UpdateAPIView):
    queryset = Game.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = ScoreGameSerializer
    permission_classes = [IsReferee]


register = RegisterView.as_view()
new_game = GameCreationView.as_view()
score_game = ScoreGameView.as_view()
