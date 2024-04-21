from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,PermissionsMixin,BaseUserManager
# from .managers import CustomUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile_number, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile_number = mobile_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile_number, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, mobile_number, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile_number, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, mobile_number, **extra_fields)

# Create your user model here.
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=128,unique=True)
    first_name = models.TextField(max_length=128)
    last_name = models.TextField(max_length=128)
    mobile_number = models.CharField(max_length=128,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # must needed, otherwise you won't be able to loginto django-admin.
    is_staff = models.BooleanField(default=True) 
    is_active = models.BooleanField(default=True)
    
    # this field we inherit from PermissionsMixin.
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ['email','first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email