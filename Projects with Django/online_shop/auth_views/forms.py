from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        fields = ['username', 'email', 'first_name']
        model=UserModel
        
