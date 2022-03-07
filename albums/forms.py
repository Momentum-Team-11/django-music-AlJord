from django import forms
from .models import Album


class Album_Form(forms.ModelForm):
        class Meta:
            model = Album
            fields = ['title', 'artist']