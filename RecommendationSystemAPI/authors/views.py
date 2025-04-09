from rest_framework import generics, viewsets, permissions

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
    permission_classes = (permissions.AllowAny,)


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    permission_classes = (permissions.AllowAny,)


class AuthorBookView(generics.ListAPIView):
    serializer_class = AuthorShortSerializer
    pagination_class = AuthorPagination
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        author_id = self.kwargs['pk']
        return Book.objects.filter(authors__id=author_id)