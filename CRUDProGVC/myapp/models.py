from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    roll = models.IntegerField()

    def __str__(self):
        return self.name
