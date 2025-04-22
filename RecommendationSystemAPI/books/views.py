from ratings.models import BookRating
from ratings.pagination import RatingPagination
from ratings.serializers import BookRatingSerializer
from rest_framework import generics, viewsets, permissions
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Book
from .pagination import BookPagination
from .serializers import BookDetailSerializer, BookShortSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookShortSerializer
    pagination_class = BookPagination
    permission_classes = (permissions.AllowAny,)


@method_decorator(cache_page(60 * 15), name='get')
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = (permissions.AllowAny,)

# TODO may be move this to ratings app
@method_decorator(cache_page(60 * 15), name='get')
class BookRatingsView(generics.ListAPIView):
    serializer_class = BookRatingSerializer
    pagination_class = RatingPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return BookRating.objects.filter(movie=movie_id)
