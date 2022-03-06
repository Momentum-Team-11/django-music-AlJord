from django.shortcuts import render, get_object_or_404
from .models import Album
from django.utils import timezone



def album_list(request):
    album= Album.objects.all()
    return render(request, 'album_list.html', {'album':album})