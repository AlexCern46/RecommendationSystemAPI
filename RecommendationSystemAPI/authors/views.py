from rest_framework import generics, viewsets

from books.models import Book
from books.pagination import BookPagination
from books.serializers import BookShortSerializer
from .models import Author
from .pagination import AuthorPagination
from .serializers import AuthorShortSerializer, AuthorDetailSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorShortSerializer
    pagination_class = AuthorPagination


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer


class AuthorBookView(generics.ListAPIView):
    serializer_class = AuthorShortSerializer
    pagination_class = AuthorPagination

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return Book.objects.filter(authors__id=author_id)