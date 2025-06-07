from django.db import models

# Create your models here.


class profile(models.Model):
    name = models.CharField(max_length=90)
    roll = models.CharField()
    email_Id = models.CharField(max_length=290)
    city = models.CharField(max_length=40)

    # def __str__(self):
    #     return self.email_Id

# here result class model create :


class Result(models.Model):
    name = models.CharField(max_length=90)
    roll = models.CharField()
    email_Id = models.CharField(max_length=290)
    mobile = models.CharField()
    city = models.CharField(230)

    # def __str__(self):
    #     return self.name
