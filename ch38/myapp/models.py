from django.db import models

# Create your models here.


from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)


class Teacher(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    T_name = models.CharField(max_length=100)
    T_mobile = models.CharField(max_length=15)
    T_age = models.CharField(max_length=3)
