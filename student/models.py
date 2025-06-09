from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(290)
    email = models.CharField(290)
    password = models.CharField(290)


# def __str__(self):
#     return self.name
