from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    active_code_email = models.CharField(max_length=94,verbose_name="کد فعال سازی ایمیل")
    avatar = models.CharField(max_length=40 , verbose_name="تصویر کاربر")
