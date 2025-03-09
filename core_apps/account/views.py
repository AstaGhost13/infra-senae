from django.shortcuts import redirect, render

# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


from core_apps.account.forms import LoginForm, SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = "account/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")  # Cambia "home" por la URL a la que deseas redirigir después del login

    def get_form_kwargs(self):
        # Elimina el argumento 'request' antes de pasarlo al formulario
        kwargs = super().get_form_kwargs()
        if 'request' in kwargs:
            del kwargs['request']
        return kwargs


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "account/register.html"
    success_url = reverse_lazy("login")  # Redirige al login después del registro

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
        return response