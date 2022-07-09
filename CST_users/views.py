# My Django imports
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

# My App imports
from CST_users.models import UserProfile
from CST_users.forms import UserForm, ProfileForm

# Create your views here.
class UserProfileView(DetailView):
    model = UserProfile
    template_name = "users/user_profile.html"

class UpdateProfileView(SuccessMessageMixin, View):
    form = UserForm
    form1 = ProfileForm

    def get(self, request, pk):
        context = {
            'form':self.form(instance=request.user),
            'form1':self.form1(instance=request.user.userprofile)
        }
        return render(request, 'users/update_profile.html', context)

    def post(self, request, pk):
        form = self.form(request.POST, instance=request.user)
        form1 = self.form1(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('users:profile', pk)

        messages.error(request, 'your response contains invalid data!')
        return render(request, 'users/update_profile', {'form':form, 'form1':form1})
