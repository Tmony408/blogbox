from django.db import models
from datetime import datetime


# Create your models here.
class Advert(models.Model):
    link= models.CharField(max_length=200, blank= True)
    link1= models.CharField(max_length=200, blank= True)
    photo1= models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank= True)
    link2= models.CharField(max_length=200, blank= True)
    photo2= models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank= True)
    link3= models.CharField(max_length=200, blank= True)
    photo3= models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank= True)
    link4= models.CharField(max_length=200, blank= True)
    photo4= models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank= True)
    link5= models.CharField(max_length=200, blank= True)
    photo5= models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank= True)
    link6= models.CharField(max_length=200, blank= True)
    photo6= models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank= True)
    link7= models.CharField(max_length=200, blank= True)
    photo7= models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank= True)
    add_date= models.DateTimeField(default=datetime.now, blank= True)
    def __str__(self):
        return self.link
