from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

#acc

class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp =models.CharField(max_length=6)
    

    

