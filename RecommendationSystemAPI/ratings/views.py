from rest_framework import generics, permissions

from .serializers import MovieRatingSerializer, BookRatingSerializer


class MovieRatingCreateView(generics.CreateAPIView):
    serializer_class = MovieRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MovieRatingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieRatingSerializer
    # TODO ovner permission for moderning rating
    permission_class = (permissions.IsAuthenticated,)


class BookRatingCreateView(generics.CreateAPIView):
    serializer_class = BookRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookRatingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookRatingSerializer
    # TODO ovner permission for moderning rating
    permission_class = (permissions.IsAuthenticated,)
