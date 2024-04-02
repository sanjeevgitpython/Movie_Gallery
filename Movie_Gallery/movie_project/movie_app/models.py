from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse


class Genre(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=250)
    poster=models.ImageField(upload_to='gallery')
    description=models.TextField()
    release_date=models.DateField()
    actors=models.TextField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE,related_name='movies')
    youtube_link=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title