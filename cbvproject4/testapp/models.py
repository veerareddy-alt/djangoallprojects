from django.db import models
from django.urls import reverse

# Create your models here.
class StudentInfo(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    addr=models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
