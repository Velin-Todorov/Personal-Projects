from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm
from django.urls import is_valid_path, reverse
from django.contrib.auth import login



# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'auth_views/login.html'
    

class RegisterView(CreateView):
    template_name='auth_views/register.html'
    form_class = UserRegistrationForm

    def get_success_url(self) -> str:
        return reverse('finish_profile')
    
class LogoutView:
    pass




