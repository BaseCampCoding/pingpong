from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from .serializers import UserCreationSerializer

User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer


register = RegisterView.as_view()
