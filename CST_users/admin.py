# My Django imports
from django.contrib import admin

# My App imports
from CST_users.models import UserProfile

# Register your models here.
admin.site.register(UserProfile)