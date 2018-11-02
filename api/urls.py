from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import register, new_game

app_name = 'api'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', register, name='register'),
    path('new-game/', new_game, name='new-game'),
]
