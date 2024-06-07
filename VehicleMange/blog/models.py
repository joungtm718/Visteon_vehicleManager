from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser



class id(AbstractUser):
    pass

class Vehicle(models.Model):
    carModel = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    mileage = models.IntegerField(default = 0)
    NowUser = models.CharField(max_length=30)
    

    
    def __str__(self) -> str:
        return self.carModel
    
class Person(models.Model):
    vekMember = models.OneToOneField(id, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.vekMember.username
# Create your models here.
