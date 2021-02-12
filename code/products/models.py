from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name