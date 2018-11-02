from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import register, new_game, score_game, users

app_name = 'api'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', register, name='register'),
    path('new-game/', new_game, name='new-game'),
    path('score-game/<id>/', score_game, name='score-game'),
    path('users/', users, name='users'),
]
