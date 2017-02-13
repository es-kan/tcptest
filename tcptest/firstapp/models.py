from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trusted = models.BooleanField(default = False)

    def __str__(self):
        return '%s (%s %s)' %(self.user.username, self.user.first_name, self.user.last_name)

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateField()
    seller = models.ForeignKey(Seller)

    def __str__(self):
        return '%s - price: %s' %(self.name, self.price)
