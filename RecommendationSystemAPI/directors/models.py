from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
