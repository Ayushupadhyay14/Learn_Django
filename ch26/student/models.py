from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    name = models.CharField()
    age = models.IntegerField()
    city = models.CharField()

    def __str__(self):
        return self.name
