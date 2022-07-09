from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid

# My App imports
from CST_users.models import UserProfile

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    body = RichTextField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, blank=True, null=True)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField()

    def __str__(self):
        return self.title