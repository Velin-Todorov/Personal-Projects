from ast import Add
from audioop import add
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import ProfileForm
from django.views.generic.edit import FormView
from .models import Profile

# Create your views here.
class CreateProfile(FormView):
    template_name='profile/create_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home')

    def form_valid(self, form) -> HttpResponse:

        if form.is_valid:
            user = self.request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']

            profile = Profile(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                user=user,
                address=address
            )

            profile.save()
            return redirect(self.success_url)
        else:
            return super().form_invalid(form)
    

class DeleteProfile:
    pass


class EditProfile:
    pass


class UpdateProfile:
    pass