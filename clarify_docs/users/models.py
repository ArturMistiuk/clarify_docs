from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    # User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
