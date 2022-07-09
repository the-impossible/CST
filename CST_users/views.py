# My Django imports
from django.shortcuts import render
from django.views.generic import DetailView

# My App imports
from CST_users.models import UserProfile
# Create your views here.
class UserProfileView(DetailView):
    model = UserProfile
    template_name = "users/user_profile.html"
