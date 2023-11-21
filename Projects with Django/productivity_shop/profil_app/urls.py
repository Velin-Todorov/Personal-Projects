from django.urls import path
from . import views

urlpatterns = [
    path('finish-your-profile', views.CreateProfile.as_view(), name='finish_profile'),
    path('profile-page/<int:pk>/', views.ProfileView.as_view(), name='profile-page')
]