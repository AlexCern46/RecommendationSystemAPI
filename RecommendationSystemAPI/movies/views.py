from ratings.models import MovieRating
from ratings.pagination import RatingPagination
from ratings.serializers import MovieRatingSerializer
from rest_framework import generics, viewsets, permissions

from .models import Movie
from .pagination import MoviePagination
from .serializers import MovieDetailSerializer, MovieShortSerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieShortSerializer
    pagination_class = MoviePagination
    permission_classes = (permissions.AllowAny,)


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = (permissions.AllowAny,)

# TODO may be ratet this to ratings app
class MovieRatingsView(generics.ListAPIView):
    serializer_class = MovieRatingSerializer
    pagination_class = RatingPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return MovieRating.objects.filter(movie=movie_id)
