from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/reg.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('home')


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}
