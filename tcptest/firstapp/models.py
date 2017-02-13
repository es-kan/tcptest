from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    date_added = models.DateField()

    def __str__(self):
        return '%s. Price: %s' %(self.name, self.price)
