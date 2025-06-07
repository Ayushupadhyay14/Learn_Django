from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default="non values")

    def __str__(self):
        return str(self.first_name)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, default="non values")

    def __str__(self):
        return str(self.first_name)
