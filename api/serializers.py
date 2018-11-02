from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from app.models import Game

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }


class UserCreationSerializer(UserSerializer):
    password_repeat = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ['password_repeat', 'token']

    def validate(self, data):
        if data['password_repeat'] != data['password']:
            raise serializers.ValidationError('Passwords must match')
        data.pop('password_repeat')
        return data

    def get_token(self, user):
        token, _created = Token.objects.get_or_create(user=user)
        return str(token)

    def save(self):
        super().save()
        self.instance.set_password(self.validated_data['password'])
        self.instance.save()


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'player_1', 'player_2', 'points', 'referee']
        read_only_fields = ['id', 'points', 'referee']


GameCreationSerializer = GameSerializer