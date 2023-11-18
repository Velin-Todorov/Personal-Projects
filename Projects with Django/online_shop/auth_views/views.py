from django.shortcuts import render
from django.contrib.auth import views as auth_views


# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'auth_views/login.html'
    

class RegisterView(auth_views.LoginView):
    template_name='auth_views/register.html'

class LogoutView:
    pass




