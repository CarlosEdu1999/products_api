from django.db import models


class Product(models.Model):
    name = models.TextField()
    category = models.TextField()
    brand = models.TextField()
    description = models.TextField()
    stock = models.IntegerField()
    active = models.BooleanField()
    image = models.ImageField()
    rating = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


