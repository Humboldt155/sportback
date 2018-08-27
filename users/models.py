from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    name = models.CharField(null=False, blank=False, max_length=255)
    refused_newsletters = models.BooleanField(null=False, blank=False) # Отказался от получать рассылки
    date_joined = models.DateTimeField(default=timezone.now) # Дата регистрации

    def __str__(self):
        return self.email
