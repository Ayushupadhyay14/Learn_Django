from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=70)

    # def __str__(self):
    #     return self.name
