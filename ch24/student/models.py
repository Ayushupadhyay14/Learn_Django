from django.db import models
from student.costum_manager import CostumManager
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=60)
    marks = models.IntegerField()
    pass_date = models.DateField()

    # def __str__(self):
    #     return self.name

    """COSTUM MANAGER FOR A USER """
    # objects = CostumManager()
    Ayush = CostumManager()
