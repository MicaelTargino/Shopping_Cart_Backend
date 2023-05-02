from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='NNR')

    def __str__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='NNR')   
    done = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.name
        