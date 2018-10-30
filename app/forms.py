from django import forms
from django.forms import Form


class RegistrationForm(Form):
    username = forms.CharField()
    password = forms.CharField()
    password_repeat = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password_repeat = cleaned_data['password_repeat']

        if password != password_repeat:
            raise forms.ValidationError('Passwords must match')

        return cleaned_data
