from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    id_serie = models.IntegerField(null=True)
    
    
