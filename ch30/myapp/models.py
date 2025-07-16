from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=300)
    city = models.IntegerField()
    Email = models.EmailField()

    def __init__(self):
        self.name
