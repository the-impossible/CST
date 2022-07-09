# My Django imports
from django import forms
from django.contrib.auth.models import User

# My app imports
from CST_users.models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']