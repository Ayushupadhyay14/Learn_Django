from django.db import models

# Create your models here.
# models.py

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.name
