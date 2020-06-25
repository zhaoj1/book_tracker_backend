from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Book

# class BookSerializer(serializers.ModelSerializer):
#   class Meta:
#     fields = (
#       'id',
#       'json',
#       'owner'
#     )
#     model = Book
class BookSerializer(serializers.Serializer):
    # title = serializers.CharField()
    # description = serializers.CharField()
    # api_id = serializers.CharField()
    # authors = serializers.CharField()
    # industryIdentifiers = serializers.CharField()
    # pageCount = serializers.IntegerField()
    # mainCategory = serializers.CharField()
    # categories = serializers.CharField()
    # infoLink = serializers.CharField()
    # averageRating = serializers.FloatField()
    # ratingsCount = serializers.IntegerField()
    class Meta:
      model = Book
      fields = (
        'id', 
        'title', 
        # 'description', 
        'api_id', 
        'authors',
        # 'industryIdentifiers',
        'isbn10',
        'isbn13',
        # 'pageCount',
        # 'mainCategory',
        # 'categories',
        # 'infoLink',
        # 'averageRating',
        # 'ratingsCount',
        'owner',
        'username'
        )
      extra_kwargs = {
        'authors': {'required': False, 'allow_blank': True},
        'industryIdentifiers': {'required': False, 'allow_blank': True},
        # 'mainCategory': {'required': False, 'allow_blank': True},
        # 'categories': {'required': False, 'allow_blank': True}
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
      # 'description', 
      'api_id', 
      'authors',
      # 'industryIdentifiers',
      'isbn10',
      'isbn13',
      # 'pageCount',
      # 'mainCategory',
      # 'categories',
      # 'infoLink',
      # 'averageRating',
      # 'ratingsCount',
      'owner',
      'username'
    )
    model = Book