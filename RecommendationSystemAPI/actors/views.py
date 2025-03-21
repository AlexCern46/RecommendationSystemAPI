from rest_framework import generics, viewsets

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


class ActorDetailView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


class ActorMovieView(generics.ListAPIView):
    serializer_class = MovieShortSerializer
    pagination_class = MoviePagination

    def get_queryset(self):
        actor_id = self.kwargs['pk']
        return Movie.objects.filter(actors__id=actor_id)
