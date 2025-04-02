from rest_framework import serializers

from .models import RecommendedMovie, RecommendedBook


class RecommendedMovieSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    movie_genre = serializers.CharField(source="movie.genre", read_only=True)

    class Meta:
        model = RecommendedMovie
        fields = ["id", "user", "movie", "movie_title", "movie_genre", "score"]


class RecommendedBookSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source="book.title", read_only=True)
    book_genre = serializers.CharField(source="book.genre", read_only=True)

    class Meta:
        model = RecommendedBook
        fields = ["id", "user", "book", "book_title", "book_genre", "score"]
