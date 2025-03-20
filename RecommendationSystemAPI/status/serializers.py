from movies.serializers import MovieShortSerializer
from rest_framework import serializers

from .models import UserMovieStatus


class UserMovieStatusSerializer(serializers.ModelSerializer):
    movie = MovieShortSerializer(read_only=True)

    class Meta:
        model = UserMovieStatus
        fields = ['movie', 'status']


class UpdateMovieStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovieStatus
        fields = ['status']
