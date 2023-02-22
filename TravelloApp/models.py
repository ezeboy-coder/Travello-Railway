from django.db import models


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    images = models.ImageField(upload_to='pics')
    special_offer = models.BooleanField(default=False)
