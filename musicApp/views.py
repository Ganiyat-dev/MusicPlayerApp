from rest_framework.viewsets import ModelViewSet
from .models import Songs
from .serializers import SongsSerializer

class SongViewSet(ModelViewSet):
    serializer_class = SongsSerializer
    queryset = Songs.objects.all()