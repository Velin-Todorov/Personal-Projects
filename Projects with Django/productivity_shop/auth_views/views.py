from typing import Self
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'auth_views/login.html'
    success_url = reverse_lazy('profile-page')
    

class RegisterView(CreateView):
    template_name='auth_views/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('finish_profile')

class LogoutView:
    pass




