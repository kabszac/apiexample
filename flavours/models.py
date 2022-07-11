from django.db import models

# Create your models here.

class Flavour(models.Model):
    name = models.CharField(max_length=50)
    orders = models.IntegerField()

    def __str__(self):
        return self.name

