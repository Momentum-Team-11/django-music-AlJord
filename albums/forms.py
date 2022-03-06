from .models import Album
from django import forms


class Album_Form(forms.ModelForm):
        class Meta:
            model = Album
            fields = [
                'Name', 
                "Band",
            ]