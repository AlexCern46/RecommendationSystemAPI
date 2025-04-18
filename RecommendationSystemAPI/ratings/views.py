from rest_framework import generics, permissions

from .serializers import MovieRatingSerializer, BookRatingSerializer
from users.pemissions import IsOwnerOrReadOnly


class MovieRatingCreateView(generics.CreateAPIView):
    serializer_class = MovieRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MovieRatingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieRatingSerializer
    permission_class = (IsOwnerOrReadOnly,)


class BookRatingCreateView(generics.CreateAPIView):
    serializer_class = BookRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookRatingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookRatingSerializer
    permission_class = (IsOwnerOrReadOnly,)
