from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)
    biography = models.TextField(null=True, blank=True)
