from rest_framework import generics, viewsets

from .models import Movie, MovieRating
from .pagination import MoviePagination, RatingPagination
from .serializers import MovieDetailSerializer, MovieShortSerializer, RatingSerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieShortSerializer
    pagination_class = MoviePagination


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


class MovieRatingsView(generics.ListAPIView):
    serializer_class = RatingSerializer
    pagination_class = RatingPagination

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return MovieRating.objects.filter(movie=movie_id)
