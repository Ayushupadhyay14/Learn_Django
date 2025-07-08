from django.db import models
from ch24.student.costum_manager import CostumManager

# ✅ Create an abstract base model


class BaseModel(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    join_date = models.DateField()

    class Meta:
        abstract = True

# ✅ Child models inherit from BaseModel


class Student(BaseModel):
    fees = models.IntegerField()  # typo: 'fess' → 'fees'


class Teacher(BaseModel):
    salary = models.IntegerField()


class Contractor(BaseModel):
    payment = models.IntegerField()
    join_date = models.DateTimeField()  # override join_date to DateTimeField


"""2️⃣ Multi-table Inheritance

Each model has its own database table.
Useful when you want to add extra fields to a base model."""


class ExamSenter(models.Model):
    center_name = models.CharField(230)
    center_city = models.CharField(230)


class Candidate(ExamSenter):  # HERE CANDIDATE ALSO NEEDTOAEXAMSENTORDETails
    name = models.CharField(230)
    roll = models.IntegerField()
