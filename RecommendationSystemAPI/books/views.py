from ratings.models import BookRating
from ratings.pagination import RatingPagination
from ratings.serializers import BookRatingSerializer
from rest_framework import generics, viewsets, permissions

from .models import Book
from .pagination import BookPagination
from .serializers import BookDetailSerializer, BookShortSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookShortSerializer
    pagination_class = BookPagination
    permission_classes = (permissions.AllowAny,)


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (permissions.AllowAny,)

# TODO may be ratet this to ratings app
class BookRatingsView(generics.ListAPIView):
    serializer_class = BookRatingSerializer
    pagination_class = RatingPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return BookRating.objects.filter(movie=movie_id)
