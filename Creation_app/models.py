from django.db import models
from .models import *


# Create your models here.
class user(models.Model):
    email = models.EmailField(max_length=50, null=True, blank= True)
    password = models.CharField(max_length=50, null=True, blank= True)

class customer(models.Model):
    name = models.CharField(max_length=50, null=True, blank= True)
    email = models.CharField(max_length=50, null=True, blank= True)
    mobile = models.CharField(max_length=50, null=True, blank= True)
    Category = models.CharField(max_length=50, null=True, blank= True)
    colour = models.CharField(max_length=50, null=True, blank= True)
    cloth_type = models.CharField(max_length=50, null=True, blank= True)
    size = models.CharField(max_length=50, null=True, blank= True)

def __str__(self):
        return self.name

class View_more(models.Model):
    dress_name = models.CharField(max_length=50, null=True, blank= True)
    category = models.CharField(max_length=50, null=True, blank= True)
    price = models.CharField(max_length=50, null=True, blank= True)
    img= models.ImageField(max_length=50, null=True, blank=True, upload_to = "media/")
    size = models.CharField(max_length=50, null=True, blank= True)


    