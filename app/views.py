from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('app:user-home')


class UserHome(TemplateView):
    template_name = 'registration.html'


registration = RegistrationView.as_view()
user_home = UserHome.as_view()
