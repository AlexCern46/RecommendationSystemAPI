from rest_framework import serializers

from actors.models import Actor
from directors.serializers import DirectorShortSerializer
from .models import Movie, MovieRating


class MovieShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = '__all__'


class ActorShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']


class MovieDetailSerializer(serializers.ModelSerializer):
    directors = DirectorShortSerializer(many=True)
    actors = ActorShortSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'directors', 'actors']
