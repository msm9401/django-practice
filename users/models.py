from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    first_name = models.CharField(max_length=150, blank=True, editable=False)
    last_name = models.CharField(max_length=150, blank=True, editable=False)
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True, blank=True)
    profile_photo = models.URLField(blank=True)
