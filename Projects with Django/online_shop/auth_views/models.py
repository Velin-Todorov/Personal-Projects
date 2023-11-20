from enum import unique
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username=None
    email = models.EmailField('email_address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



class Profile(models.Model):
    """
    Model that contains app-specific info about the user
    """
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
