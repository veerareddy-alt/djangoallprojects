from django.db import models
from django import forms

# Create your models here.
class HomeModel(models.Model):
    coursename=models.CharField(max_length=30)
    quantity=models.IntegerField()
