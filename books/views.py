from django.shortcuts import render

from rest_framework import generics

from .models import Book
from .serializers import BookSerializer

class ListBook(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer