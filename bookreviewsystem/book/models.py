from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('technology', 'Technology'),
        ('history', 'History'),
    ]

    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    publication_date = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MaxValueValidator(5), MinValueValidator(0)],
        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})


# from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.urls import reverse

# # Create your models here.


# class Book(models.Model):
#     GENERAL_CHOICE = [
#         ('fiction', 'Fiction'),
#         ('non_fiction', 'Non_Fiction'),
#         ('science', 'Science'),
#         ('technology', 'Technology'),
#         ('history', 'History'),
#     ]


# title = models.CharField(max_length=300)
# author = models.CharField(max_length=200)
# description = models.TextField()
# genre = models.CharField(max_length=20, choices='GENERAL_CHOICE')
# isbn = models.CharField('ISBN', max_length=13, unique=True)
# publication_date = models.DecimalField(
#     max_digits=3,
#     decimal_places=2,
#     validators=[MaxValueValidator(5), MinValueValidator(0)],
#     default=0
# )
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)


# def __str__(self):
#     return self.title


# def get_absolute_url(self):
#     return reverse("book_detail", kwargs={"pk": self.pk})
