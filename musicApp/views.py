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

    

class SongsAPIView(APIView):   
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongsDetails(APIView):
    def get_object(self, id):
        try:
            return Songs.objects.get(id=id)

        except Songs.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        songs = self.get_obeject(id)
        serializer = SongsSerializer(songs)
        return Response(serializer.data)

    def put(self, request, id):
        songs = self.get_obeject(id)
        serializer = SongsSerializer(songs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        songs = self.get_obeject(id)
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


