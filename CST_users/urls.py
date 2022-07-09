# My Django imports
from django.urls import path

# My App imports
from CST_users.views import (
    UserProfileView,
    UpdateProfileView,
)

app_name = 'users'

urlpatterns = [
    path('profile/<pk>', UserProfileView.as_view(), name='profile'),
    path('profile_edit/<pk>', UpdateProfileView.as_view(), name='profile_edit'),
]