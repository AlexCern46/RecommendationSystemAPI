from django.shortcuts import render
from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer


class AuthorList(generics.ListCreateAPIView):
    """
    List all authors, or create a new author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a author instance.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
