# Song Serializers
from rest_framework.serializers import ModelSerializer
from .models import Songs

class SongsSerializer(ModelSerializer):
  class Meta:
    model = Songs
    fields = '__all__'
