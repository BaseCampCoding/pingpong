from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model

from .forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('app:user-home')

    def form_valid(self, form):
        UserModel = get_user_model()
        UserModel.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        return super().form_valid(form)


class UserHome(TemplateView):
    template_name = 'registration.html'


class Login(LoginView):
    template_name = 'login.html'


registration = RegistrationView.as_view()
user_home = UserHome.as_view()
login = Login.as_view()