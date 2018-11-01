from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('user/', views.user_home, name='user-home'),
    path('new-game/', views.new_game, name='new-game'),
    path('game/<id>/', views.game, name='game'),
    path('game/<id>/score', views.score_game, name='score-game'),
]
