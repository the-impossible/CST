# My Django imports
from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

# My App imports
from CST_users.models import UserProfile
from CST_auth.forms import RegisterForm

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username').strip().lower()
        password = request.POST.get('password')

        if username and password:
            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'You are now signed in {user.get_full_name()}')
                    return redirect('users:profile', user.userprofile.profile_id)
                else:
                    messages.warning(request, 'Account not active contact the administrator')
                    return redirect('auth:login')
            else:
                messages.warning(request, 'Invalid login credentials')
                return redirect('auth:login')
        else:
            messages.error(request, 'All fields are required!!')
            return redirect('auth:login')

class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, 'You are successfully logout, to continue login again')

        return redirect('auth:login')

class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_message = "Account Created Successfully! You can now login"
    success_url = 'login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.email = self.object.email.strip().lower()
        self.object.username = self.object.username.strip().lower()
        self.object.save()
        UserProfile.objects.create(user=self.object)

        return HttpResponseRedirect(self.get_success_url())