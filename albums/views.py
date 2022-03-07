from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from django.utils import timezone
from .forms import Album_Form


def album_list(request):
    album= Album.objects.all()
    return render(request, 'album_list.html', {'album':album})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = Album_Form()
    return render(request, 'album_detail.html', {'album':album, 'form':form})

def add_album(request):
    if request.method == 'GET':
        form = Album_Form()
    else:
        form= Album_Form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='add_album')
    return render(request, 'add_album.html', {'form':form})

def edit_album(request, pk):
    album= get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        form = Album_Form(instance=album)
    else:
        form = Album_Form(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
        return redirect(to='album_list')
    return render(request, 'edit_album.html', {
        'form': form,
        "album": album
    })

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect(to='album_list')
    return render(request, 'delete_album.html', {'album': album})