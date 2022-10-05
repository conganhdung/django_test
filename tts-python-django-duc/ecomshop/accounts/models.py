from asyncio import FastChildWatcher
from turtle import update
from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    update =  models.DateTimeField(blank=False, null=True)

