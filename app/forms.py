from django import forms
from django.forms import Form


class RegistrationForm(Form):
    username = forms.CharField()
    password = forms.CharField()
    password_repeat = forms.CharField()
