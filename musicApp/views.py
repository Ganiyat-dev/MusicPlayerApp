from django.shortcuts import render, redirect

# import models here
from django.core.paginator import Paginator
from .models import Song
# Create your views here.

def index(request):
    song_profile = Song.objects.get_queryset().order_by('id')
    paginator = Paginator(song_profile, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, 'index.html', context)
