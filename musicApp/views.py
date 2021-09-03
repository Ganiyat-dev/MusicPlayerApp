# from django.shortcuts import render, redirect

# # import models here
# from django.core.paginator import Paginator
# from .models import Song
# # Create your views here.

# def index(request):
#     song_profile = Song.objects.get_queryset().order_by('id')
#     paginator = Paginator(song_profile, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {"page_obj": page_obj}
#     return render(request, 'index.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Songs
from django.db.models import query
from rest_framework import generics, serializers, status
from .serializers import SongsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class Songsview(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

