from rest_framework import generics, viewsets, permissions

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
    permission_classes = (permissions.AllowAny,)


class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer
    permission_classes = (permissions.AllowAny,)


class DirectorMovieView(generics.ListAPIView):
    serializer_class = MovieShortSerializer
    pagination_class = MoviePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        director_id = self.kwargs['pk']
        return Movie.objects.filter(directors__id=director_id)
