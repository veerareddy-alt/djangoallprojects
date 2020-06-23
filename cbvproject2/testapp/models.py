from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=256)
    author=models.CharField(max_length=60)
    pages=models.IntegerField()
    price=models.FloatField()
