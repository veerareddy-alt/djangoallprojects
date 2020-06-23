import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","crudfb2vproject.settings")
import django
django.setup()
from testapp.models import *
from faker import Faker

from random import *
f=Faker()

def populate(n):
    for i in range(n):
        fsrollno=randint(1001,9999)
        fsname=f.name()
        fsdept=f.city()

        stu_record= Student.objects.get_or_create(srollno=fsrollno,sname=fsname,sdept=fsdept,)
populate(20)
