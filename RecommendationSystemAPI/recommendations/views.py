from rest_framework import viewsets
from rest_framework import permissions

from .models import RecommendedMovie, RecommendedBook
from .serializers import RecommendedMovieSerializer, RecommendedBookSerializer


class RecommendedMovieViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RecommendedMovieSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return RecommendedMovie.objects.filter(user=self.request.user)


class RecommendedBookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RecommendedBookSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return RecommendedBook.objects.filter(user=self.request.user)
