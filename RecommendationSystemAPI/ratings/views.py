from rest_framework import generics

from .serializers import MovieRatingSerializer, BookRatingSerializer


class MovieRatingCreateView(generics.CreateAPIView):
    serializer_class = MovieRatingSerializer
    permission_classes = None


class MovieRatingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieRatingSerializer
    permission_class = None


class BookRatingCreateView(generics.CreateAPIView):
    serializer_class = BookRatingSerializer
    permission_classes = None


class BookRatingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookRatingSerializer
    permission_class = None
