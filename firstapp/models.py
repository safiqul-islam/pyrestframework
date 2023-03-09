from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=4)
