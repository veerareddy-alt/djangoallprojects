from django.db import models
class CoustomManger1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=25000)

class CoustomManger2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')

class CoustomManger3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('esal')
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=64)
    objects=CoustomManger1()

class ProxyEmployee(Employee):
    objects=CoustomManger2()
    class Meta:
        proxy=True


class ProxyEmployee2(Employee):
    objects=CoustomManger2()
    class Meta:
        proxy=True
