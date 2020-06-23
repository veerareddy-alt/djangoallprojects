from django.db import models


# Create your models here.
class EmpModel(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
