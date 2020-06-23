from django.db import models

# Create your models here.
class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=20)
    actor=models.CharField(max_length=20)
    actress=models.CharField(max_length=20)
    rating=models.IntegerField()
