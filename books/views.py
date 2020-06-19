# # from django.shortcuts import render

# # from rest_framework import generics

# # from .models import Book
# # from .serializers import BookSerializer

# # class ListBook(generics.ListCreateAPIView):

# #   # def get_queryset(self):
# #   #   user = self.request.user
# #   #   return Book.objects.filter(owner=user)

# #   queryset = Book.objects.all()
# #   serializer_class = BookSerializer

# # class DetailBook(generics.RetrieveUpdateDestroyAPIView):
# #   queryset = Book.objects.all()
# #   serializer_class = BookSerializer

# from django.http import HttpResponseRedirect
# from rest_framework import permissions, status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import BookSerializer, BookSerializerWithToken

# @api_view(['GET'])
# def current_book(request):
#   serializer = BookSerializer(request.auth)
#   return Response(serializer.data)

# class BookList(APIView):
#   permission_classes = (permissions.AllowAny,)

#   def post(self, request, format=None):
#     serializer = BookSerializerWithToken(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import permissions, status

from .models import Book
from .serializers import BookSerializerWithToken

class BookView(APIView):
  def get(self, request):
    books = Book.objects.all()
    serializer = BookSerializerWithToken(books, many=True)
    return Response({'books':serializer.data})

  # def post(self, request):
  #   serializer = BookSerializerWithToken(data=book)
  #   if serializer.is_valid(raise_exception=True):
  #     book_saved = serializer.save()
  #   return Response({'success':"Book `{}` created successfully".format(book_saved.title)})
  
  def delete(self, request, pk):
    book = get_object_or_404(Book.objects.all(),pk=pk)
    book.delete()
    return Response({'message':"Book with id `{}` has been deleted.".format(pk)},status=204)

class BookList(APIView):
  permission_classes = (permissions.AllowAny,)
  def post(self, request, format=None):
    serializer = BookSerializerWithToken(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)