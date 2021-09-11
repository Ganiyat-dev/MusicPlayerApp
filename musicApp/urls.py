from rest_framework.routers import DefaultRouter
from .views import SongViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('songs', SongViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]