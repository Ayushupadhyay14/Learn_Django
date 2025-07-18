from django.db import models
from django.utils.translation import gettext_lazy as _


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=10)
    course = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_images/')
# ImageField usage

    def __str__(self):
        return self.name
