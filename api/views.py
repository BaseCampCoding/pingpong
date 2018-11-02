from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from app.models import Game
from rest_framework.permissions import IsAuthenticated

from .serializers import UserCreationSerializer, GameCreationSerializer

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


register = RegisterView.as_view()
new_game = GameCreationView.as_view()
