from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    discord = models.CharField(max_length=255, blank=False, null=False, default='')
    twitter = models.CharField(max_length=255, blank=False, null=False, default='')
    twitch = models.CharField(max_length=255, blank=False, null=False, default='')


class Game(models.Model):
    game_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False)
    title = models.CharField(max_length=255, blank=False, null=False, default='')
    release_date = models.DateField(blank=True, null=True)
    platform = models.CharField(max_length=255, blank=False, null=False, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Game'


class Run(models.Model):
    run_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=False, null=False, default='')
    game_ID = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ava.gameid+')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.run_ID)

    class Meta:
        verbose_name = 'Run'
        verbose_name_plural = 'Run'
