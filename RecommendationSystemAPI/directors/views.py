from rest_framework import generics, viewsets

from movies.models import Movie
from movies.pagination import MoviePagination
from movies.serializers import MovieShortSerializer
from .models import Director
from .pagination import DirectorPagination
from .serializers import DirectorShortSerializer, DirectorDetailSerializer


class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorShortSerializer
    pagination_class = DirectorPagination


class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer


class DirectorMovieView(generics.ListAPIView):
    serializer_class = MovieShortSerializer
    pagination_class = MoviePagination

    def get_queryset(self):
        director_id = self.kwargs['pk']
        return Movie.objects.filter(directors__id=director_id)
