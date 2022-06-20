from django.db import models

class Anime(models.Model):
        name = models.CharField(max_length = 255)
        description = models.CharField(max_length=1000)
        episodes = models.CharField(max_length=6)

