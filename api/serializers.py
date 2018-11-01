from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        write_only_fields = ['password']


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
        return str(Token.objects.get_or_create(user=user))
