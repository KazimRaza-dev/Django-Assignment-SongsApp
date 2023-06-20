from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('enduser', 'End-User'),        # (storedValue, humanReadable value)
        ('admin', 'Admin'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'password', 'user_type',
                       'first_name', 'last_name')

    def __str__(self):
        return f"{self.username}({self.id})"
