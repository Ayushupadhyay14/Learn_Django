from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField()
    password = models.CharField()


# def __str__(self):
#     return self.name
