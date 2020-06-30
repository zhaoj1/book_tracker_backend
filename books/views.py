from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializerWithToken

class BookView(APIView):
  permission_classes = (permissions.AllowAny)
  http_method_names = ['get', 'head']
  
  def delete(self, request, pk):
    book = get_object_or_404(Book.objects.all(),pk=pk)
    book.delete()
    return Response({'message':"Book with id `{}` has been deleted.".format(pk)},status=204)

class BookList(APIView):

  def get(self, request):
    books = list(filter(lambda x: x.owner == request.user.id, Book.objects.all()))
    serializer = BookSerializerWithToken(books, many=True)
    return Response({'books':serializer.data})

  def post(self, request, format=None):
    serializer = BookSerializerWithToken(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)