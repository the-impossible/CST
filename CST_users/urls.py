# My Django imports
from django.urls import path

# My App imports
from CST_users.views import (
    UserProfileView,
)

app_name = 'users'

urlpatterns = [
    path('profile/<pk>', UserProfileView.as_view(), name='profile'),
]