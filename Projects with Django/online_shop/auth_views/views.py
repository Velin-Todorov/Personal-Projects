from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm


# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'auth_views/login.html'
    

class RegisterView(CreateView):
    template_name='auth_views/register.html'
    form_class = UserRegistrationForm

    

class LogoutView:
    pass




