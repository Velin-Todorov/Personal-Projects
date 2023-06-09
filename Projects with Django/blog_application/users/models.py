from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Uuser(models.Model):
    
    class Verified(models.TextChoices):
        YES = 'Y', 'Yes'
        NO = 'N', 'No'

    class Meta:
        db_table = 'users'

    username = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2,
        choices=Verified.choices,
        default=Verified.NO
    )
    followers = models.BigIntegerField(default=0)
    
