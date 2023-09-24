from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings



class CustomUser(AbstractUser):
    username = models.CharField(max_length=1024, unique=True)
    password = models.CharField(max_length=1024, unique=True)

    def __str__(self):
        return self.username