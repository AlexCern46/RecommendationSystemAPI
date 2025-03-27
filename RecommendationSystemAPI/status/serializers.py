from books.serializers import BookShortSerializer
from movies.serializers import MovieShortSerializer
from rest_framework import serializers

from .models import UserMovieStatus, UserBookStatus


class UserMovieStatusSerializer(serializers.ModelSerializer):
    movie = MovieShortSerializer(read_only=True)

    class Meta:
        model = UserMovieStatus
        fields = ['movie', 'status']


class UpdateMovieStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovieStatus
        fields = ['status']


class UserBookStatusSerializer(serializers.ModelSerializer):
    book = BookShortSerializer(read_only=True)

    class Meta:
        model = UserBookStatus
        fields = ['book', 'status']


class UpdateBookStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookStatus
        fields = ['status']
