from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import register

app_name = 'api'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', register, name='register'),
]
