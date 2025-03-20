from django.db import models


class Author(models.Model):
    """
    fields:
        name - VARCHAR(255), not null
        birthdate - DATE
        biography - TEXT
    """
    name = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
