from django.db import models

# Create your models here.
class Student(models.Model):
    srollno=models.IntegerField()
    sname=models.CharField(max_length=30)
    sdept=models.CharField(max_length=30)
    
