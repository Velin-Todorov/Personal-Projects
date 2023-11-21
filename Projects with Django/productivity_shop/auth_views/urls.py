from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login_view'),
    path('register', views.RegisterView.as_view(), name='register_view')
]
