from django.db import models
from django.utils import timezone

class Album(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    artist = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title