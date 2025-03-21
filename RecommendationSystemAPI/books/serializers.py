from rest_framework import serializers

from authors.serializers import AuthorShortSerializer
from .models import Book


class BookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'cover']


class BookDetailSerializer(serializers.ModelSerializer):
    actors = AuthorShortSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
