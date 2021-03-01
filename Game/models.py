from django.conf import settings
from django.db import models


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    PLATFORMS = (('NES', 'NES'),
                 ('SNES', 'SNES'),
                 ('GBC', 'Gameboy Color'),
                 ('NDS', 'Nintendo DS'),
                 ('3DS', 'Nintendo 3DS'),
                 ('N64', 'N64'),
                 ('NSW', 'Nintendo Switch'),
                 ('PS2', 'PS2'),
                 ('PS3', 'PS3'),
                 ('PS4', 'PS4'),
                 ('XBOX1', 'Xbox 1'),
                 ('XBOX3', 'Xbox 360'),
                 ('PC', 'PC'),
                 ('IP', 'Iphone'),
                 ('AND', 'Android'),
                 )
    platform = models.CharField(max_length=50, choices=PLATFORMS)
    release_date = models.DateTimeField(blank=True, null=True)
