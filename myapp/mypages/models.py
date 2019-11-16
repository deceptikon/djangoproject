from django.db import models

# Create your models here.

# https://docs.djangoproject.com/en/2.2/ref/models/fields/

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    discount = models.BooleanField()
    description = models.TextField(default=None)

    def __str__(self):
        return self.name

# python manage.py makemigrations mypages
# python manage.py migrate mypages
