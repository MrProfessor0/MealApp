from django.db import models

# Create your models here.

class Mess(models.Model):
    """
    Model for storing mess data.
    """
    # id = models.IntegerField(primary_key=True,)
    id = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=255,unique=True)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

