from django.contrib.auth import get_user_model
from django.db import models

from movies.models import Movie

User = get_user_model()


class MovieStatus(models.TextChoices):
    NOT_WATCHED = 'not_watched'
    WATCHING = 'watched'
    DROPPED = 'dropped'
    PLANNED = 'planned'


class UserMovieStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=MovieStatus.choices,
        default=MovieStatus.NOT_WATCHED
    )

    class Meta:
        unique_together = ('user', 'movie')
