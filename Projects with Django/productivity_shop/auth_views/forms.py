from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        fields = ['username', 'email', 'password1', 'password2']
        model=UserModel
        
