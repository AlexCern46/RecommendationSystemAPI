from rest_framework import generics, viewsets, permissions
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from movies.models import Movie
from movies.pagination import MoviePagination
from movies.serializers import MovieShortSerializer
from .models import Actor
from .pagination import ActorPagination
from .serializers import ActorShortSerializer, ActorDetailSerializer


class ActorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorShortSerializer
    pagination_class = ActorPagination
    permission_classes = (permissions.AllowAny,)


@method_decorator(cache_page(60 * 15), name='get')
class ActorDetailView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
    permission_classes = (permissions.AllowAny,)


@method_decorator(cache_page(60 * 15), name='get')
class ActorMovieView(generics.ListAPIView):
    serializer_class = MovieShortSerializer
    pagination_class = MoviePagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        actor_id = self.kwargs['pk']
        return Movie.objects.filter(actors__id=actor_id)
