from django.shortcuts import get_object_or_404
from movies.models import Movie
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from .models import UserMovieStatus, MovieStatus
from .serializers import UserMovieStatusSerializer, UpdateMovieStatusSerializer


class UpdateMovieStatusView(generics.UpdateAPIView):
    serializer_class = UpdateMovieStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        movie_id = self.kwargs['movie_id']
        movie = get_object_or_404(Movie, id=movie_id)
        obj, _ = UserMovieStatus.objects.get_or_create(user=self.request.user, movie=movie)
        return obj


class MoviesByStatusView(generics.ListAPIView):
    serializer_class = UserMovieStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get('status', MovieStatus.PLANNED)
        return UserMovieStatus.objects.filter(user=self.request.user, status=status)
