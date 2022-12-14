from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyClubUser(models.Model):
    first_name = models.CharField('User First Name', max_length=64, null=False)
    email =models.EmailField('User Email', max_length=64)

    def __str__(self):
        return self.first_name

class Vehicle(models.Model):
    owner = models.ForeignKey(User,blank = False, on_delete=models.PROTECT,related_name="user_creator")
    plate = models.CharField(max_length=50)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.plate