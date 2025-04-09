from books.models import Book
from django.shortcuts import get_object_or_404
from movies.models import Movie
from rest_framework import generics, permissions

from .models import UserMovieStatus, MovieStatus, BookStatus, UserBookStatus
from .serializers import UserMovieStatusSerializer, UpdateMovieStatusSerializer, UpdateBookStatusSerializer


class UpdateMovieStatusView(generics.UpdateAPIView):
    serializer_class = UpdateMovieStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        movie_id = self.kwargs['movie_id']
        movie = get_object_or_404(Movie, id=movie_id)
        obj, _ = UserMovieStatus.objects.get_or_create(user=self.request.user, movie=movie)
        return obj


class MoviesByStatusView(generics.ListAPIView):
    serializer_class = UserMovieStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        status = self.request.query_params.get('status', MovieStatus.PLANNED)
        return UserMovieStatus.objects.filter(user=self.request.user, status=status)


class UpdateBookStatusView(generics.UpdateAPIView):
    serializer_class = UpdateBookStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        book_id = self.kwargs['book_id']
        book = get_object_or_404(Book, id=book_id)
        obj, _ = UserBookStatus.objects.get_or_create(user=self.request.user, book=book)
        return obj


class BooksByStatusView(generics.ListAPIView):
    serializer_class = UpdateBookStatusSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        status = self.request.query_params.get('status', BookStatus.PLANNED)
        return UserBookStatus.objects.filter(user=self.request.user, status=status)
