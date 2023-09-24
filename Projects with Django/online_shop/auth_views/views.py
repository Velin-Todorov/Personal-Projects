from django.shortcuts import render
from django.contrib.auth import views as auth_views
from cuser.models import CUser

# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'auth_views/login.html'
    

class RegisterView:
    pass

class LogoutView:
    pass




