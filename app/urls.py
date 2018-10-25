from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('user/', views.user_home, name='user-home'),
]
