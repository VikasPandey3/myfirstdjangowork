from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string


class Iot(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    pin_no = models.CharField(max_length=2, default="0", null=True, blank=True,)
    state = models.CharField(max_length=3, default="OFF", null=True, blank=True)
    pin3 = models.CharField(max_length=5, default="OFF")
    pin5 = models.CharField(max_length=5, default="OFF")
    pin7 = models.CharField(max_length=5, default="OFF")
    pin11 = models.CharField(max_length=5, default="OFF")
    pin13 = models.CharField(max_length=5, default="OFF")
    pin15 = models.CharField(max_length=5, default="OFF")
    pin19 = models.CharField(max_length=5, default="OFF")
    pin21 = models.CharField(max_length=5, default="OFF")

    def __str__(self):
        return self.id


class CustomUser(AbstractUser):
    api_key = models.CharField(max_length=100, default=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(18)))

    def __str__(self):
        return self.username
