from rest_framework import serializers

from actors.serializers import ActorShortSerializer
from directors.serializers import DirectorShortSerializer
from .models import Movie


class MovieShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'poster']


class MovieDetailSerializer(serializers.ModelSerializer):
    directors = DirectorShortSerializer(many=True)
    actors = ActorShortSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
