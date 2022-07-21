# My Django imports
from django.urls import path

# My App imports
from CST_auth.views import (
    LoginView,
    LogoutView,
    RegisterView,
)

app_name = 'auth'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
]
