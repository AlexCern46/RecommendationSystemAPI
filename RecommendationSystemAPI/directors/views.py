from rest_framework import generics, viewsets, permissions
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

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


@method_decorator(cache_page(60 * 15), name='get')
class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer
    permission_classes = (permissions.AllowAny,)


@method_decorator(cache_page(60 * 15), name='get')
class DirectorMovieView(generics.ListAPIView):
    serializer_class = MovieShortSerializer
    pagination_class = MoviePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        director_id = self.kwargs['pk']
        return Movie.objects.filter(directors__id=director_id)
