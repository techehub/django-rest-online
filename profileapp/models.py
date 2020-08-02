from django.db import models

# Create your models here.


class Profile (models. Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone= models.CharField(max_length=10)
    email= models.EmailField(max_length=100)