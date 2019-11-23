from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.utils import timezone

# All table schemas are defined here.

class Account(AbstractBaseUser):
    account_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="email", max_length=30, unique=True)



# class TravelNote(models.Model):
