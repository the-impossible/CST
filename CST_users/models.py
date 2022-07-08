# My Django imports
from django.db import models
from django.contrib.auth.models import User
import uuid
# My App imports

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images', blank=True, null=True)
    about = models.TextField()
    profile_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.user.username

