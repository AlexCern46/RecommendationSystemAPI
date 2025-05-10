from rest_framework import serializers

from .models import MovieRating, BookRating


class MovieRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRating
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Invalid value")
        return value


class BookRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Invalid value")
        return value
