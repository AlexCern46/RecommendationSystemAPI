import uuid

from authors.models import Author
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')
    release_year = models.IntegerField()
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.cover:
            ext = self.cover.name.split('.')[-1]
            unique_name = f"{uuid.uuid4()}.{ext}"
            self.cover.name = f"covers/{unique_name}"
        super().save(*args, **kwargs)
