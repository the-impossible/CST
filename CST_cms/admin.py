from django.contrib import admin

# My app imports
from CST_cms.models import (
    Post,
)

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)