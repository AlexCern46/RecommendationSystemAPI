import uuid

from actors.models import Actor
from directors.models import Director
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    directors = models.ManyToManyField(Director, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    release_year = models.IntegerField()
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.poster:
            ext = self.poster.name.split('.')[-1]
            unique_name = f"{uuid.uuid4()}.{ext}"
            self.poster.name = f"posters/{unique_name}"
        super().save(*args, **kwargs)
