
from django.db import models

# Create your models here.
class Donation(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    amount = models.DecimalField(max_digits=3, decimal_places=2)