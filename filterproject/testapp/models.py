from django.db import models

# Create your models here.
class Filtermodel(models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    dept=models.CharField(max_length=20)
    date=models.DateField()
