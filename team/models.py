from django.db import models
from datetime import datetime


# Create your models here.
class Team(models.Model):
    name= models.CharField(max_length= 200)
    email= models.EmailField(max_length= 50)
    telephone= models.CharField(max_length=20)
    description= models.TextField(blank=True)
    hire_date= models.DateTimeField(default=datetime.now, blank= True)
    photo_main= models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    is_mvp= models.BooleanField(default=False)
    def __str__(self):
        return self.name
