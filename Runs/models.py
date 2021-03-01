from django.conf import settings
from django.db import models


class Runs(models.Model):
    run_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=20)
    user_id = models.ForeignKey(on_delete=models.CASCADE,)
    game_id = models.ForeignKey(on_delete=models.CASCADE,)