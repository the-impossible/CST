# My Django imports
from django import forms
from django.contrib.auth.models import User

# My app imports
from CST_users.models import UserProfile

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']