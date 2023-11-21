from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import ProfileForm
from django.views.generic.edit import FormView
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
class CreateProfile(CreateView):
    template_name='profile/create_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile-page')
    

class DeleteProfile:
    pass


class EditProfile:
    pass


class UpdateProfile:
    pass


class ProfileView(DetailView):
    template_name='profile/profile.html'
    model = Profile