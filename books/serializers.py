from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Book

class BookSerializer(serializers.Serializer):
    class Meta:
      model = Book
      fields = (
        'id', 
        'title', 
        'api_id', 
        'authors',
        'imageLink',
        'isbn10',
        'isbn13',
        'owner',
        'username',
        'totalPages',
        'pagesRead'
        )
      extra_kwargs = {
        'authors': {'required': False, 'allow_blank': True},
        'industryIdentifiers': {'required': False, 'allow_blank': True},
      } 

class BookSerializerWithToken(serializers.ModelSerializer):
  
  token = serializers.SerializerMethodField()

  def get_token(self, obj):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(obj)
    token = jwt_encode_handler(payload)
    return token

  def create(self, validated_data):
    instance = self.Meta.model(**validated_data)
    instance.save()
    return instance

  class Meta:
    fields = (
      'token',
      'id', 
      'title', 
      'api_id', 
      'authors',
      'imageLink',
      'isbn10',
      'isbn13',
      'owner',
      'username',
      'totalPages',
      'pagesRead'
    )
    model = Book