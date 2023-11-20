from django.db import models
from django.contrib.auth.models import User


# Create your models here.
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