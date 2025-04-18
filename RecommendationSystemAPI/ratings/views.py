from rest_framework import generics, permissions, serializers

from .models import MovieRating, BookRating
from .serializers import MovieRatingSerializer, BookRatingSerializer
from users.pemissions import IsOwnerOrReadOnly


class MovieRatingCreateView(generics.CreateAPIView):
    serializer_class = MovieRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        movie = serializer.validated_data['movie']
        if MovieRating.objects.filter(user=self.request.user, movie=movie).exists():
            raise serializers.ValidationError("Only one rev")
        serializer.save(user=self.request.user)


class MovieRatingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieRatingSerializer
    permission_class = (IsOwnerOrReadOnly,)
    queryset = MovieRating.objects.select_related('user', 'movie')

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )


class BookRatingCreateView(generics.CreateAPIView):
    serializer_class = BookRatingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        movie = serializer.validated_data['book']
        if BookRating.objects.filter(user=self.request.user, movie=movie).exists():
            raise serializers.ValidationError("Only one rev")
        serializer.save(user=self.request.user)


class BookRatingView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookRatingSerializer
    permission_class = (IsOwnerOrReadOnly,)
    queryset = BookRating.objects.select_related('user', 'book')

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user
        )
