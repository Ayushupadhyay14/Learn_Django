from django.db import models
from django.urls import reverse
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=23)
    email = models.EmailField()
    password = models.CharField(max_length=40)


def get_absolute_url(self):
    return reverse('thanks1')
