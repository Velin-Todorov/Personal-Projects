from django.urls import path
from . import views

urlpatterns = [
    path('finish-your-profile', views.CreateProfile.as_view(), name='finish_profile')
]