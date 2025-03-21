from ratings.models import BookRating
from ratings.pagination import RatingPagination
from ratings.serializers import BookRatingSerializer
from rest_framework import generics, viewsets

from .models import Book
from .pagination import BookPagination
from .serializers import BookDetailSerializer, BookShortSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookShortSerializer
    pagination_class = BookPagination


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookRatingsView(generics.ListAPIView):
    serializer_class = BookRatingSerializer
    pagination_class = RatingPagination

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return BookRating.objects.filter(movie=movie_id)
