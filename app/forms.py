from django import forms
from django.forms import Form, ModelForm
from django.contrib.auth import get_user_model

from . import models


class RegistrationForm(ModelForm):
    password_repeat = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password_repeat = cleaned_data['password_repeat']

        if password != password_repeat:
            raise forms.ValidationError('Passwords must match')

        return cleaned_data


class GameUpdateForm(ModelForm):
    point_1 = forms.IntegerField()
    point_2 = forms.IntegerField()
    point_3 = forms.IntegerField()
    point_4 = forms.IntegerField()
    point_5 = forms.IntegerField()
    point_6 = forms.IntegerField()
    point_7 = forms.IntegerField()
    point_8 = forms.IntegerField()
    point_9 = forms.IntegerField()
    point_10 = forms.IntegerField()
    point_11 = forms.IntegerField(required=False)
    point_12 = forms.IntegerField(required=False)
    point_13 = forms.IntegerField(required=False)
    point_14 = forms.IntegerField(required=False)
    point_15 = forms.IntegerField(required=False)
    point_16 = forms.IntegerField(required=False)
    point_17 = forms.IntegerField(required=False)
    point_18 = forms.IntegerField(required=False)
    point_19 = forms.IntegerField(required=False)

    class Meta:
        model = models.Game
        fields: list = []

    def clean(self):
        cleaned_data = super().clean()
        return {'points': GameUpdateForm.point_fields_to_list(cleaned_data)}

    def save(self):
        self.instance.points = self.cleaned_data['points']
        return super().save()

    @staticmethod
    def point_fields_to_list(cleaned_data):
        return [
            winner for point, winner in sorted(
                cleaned_data.items(),
                key=lambda field: int(field[0].split('_')[1])) if winner
        ]
