# models.py
from django.contrib.auth.models import User
from django.db import models

class Visit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)