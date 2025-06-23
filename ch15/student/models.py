from django.db import models

# Create your models here.


class product(models.Model):
    name = models.CharField(max_length=244)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
