from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    address=models.CharField(max_length=256)
    class Meta:
        abstract=True


class Student(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(ContactInfo):
    subjects=models.CharField(max_length=30)
    salary=models.FloatField()



class ContactInfo1(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    address=models.CharField(max_length=256)



class Student2(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher2(ContactInfo):
    subjects=models.CharField(max_length=30)
    salary=models.FloatField()



class ContactInfo2(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    address=models.CharField(max_length=256)



class StudentII(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class TeacherII(ContactInfo):
    subjects=models.CharField(max_length=30)
    salary=models.FloatField()


class ContactInfo3(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    address=models.CharField(max_length=256)



class StudentIII(ContactInfo3):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class TeacherIII(ContactInfo3):
    subjects=models.CharField(max_length=30)
    salary=models.FloatField()

class Parent1(models.Model):
    fd1=models.CharField(max_length=256)
    fd2=models.CharField(max_length=256)

class Child(Parent1):
    fd3=models.CharField(max_length=256)
    fd4=models.CharField(max_length=256)

class SubChild(Child):
    fd5=models.CharField(max_length=256)
