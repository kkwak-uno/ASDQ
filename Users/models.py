from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=False, null=False, default=' ')
    email = models.CharField(max_length=100, blank=False, null=False, default=' ')
    country = CountryField()
    discord = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    twitch = models.CharField(max_length=100, blank=True, null=True)
