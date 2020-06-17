from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Book

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'id',
      'book',
      'owner'
    )
    model = Book

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
    return instance

  class Meta:
    fields = (
      'token',
      'id',
      'book',
      'owner'
    )
    model = Book