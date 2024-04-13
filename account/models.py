from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,PermissionsMixin
from .managers import CustomUserManager

# Create your models here.
# class User(AbstractBaseUser,PermissionsMixin):
#     first_name = models.TextField(max_length=128)
#     last_name = models.TextField(max_length=128)
#     email = models.EmailField(max_length=128,unique=True)
#     phone_number = models.EmailField(max_length=128)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
    
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email