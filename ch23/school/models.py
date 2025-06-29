from django.db import models

# Create your models here.
# here create a model in Student name and describe a fiels for a studemt model:


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=200)
    marks = models.IntegerField()
    pass_date = models.DateField()

# here create a model Teacher name and describe a all fiels for a teacher relaited :

class Teacher(models.Model):
    name = models.CharField(max_length=60)
    empnum = models.CharField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()
