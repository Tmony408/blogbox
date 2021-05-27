from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=200)
    subject= models.CharField(max_length=400)
    email= models.EmailField(max_length= 50)
    message= models.TextField()
    contact_date= models.DateTimeField(default=datetime.now, blank= True)
    def __str__(self):
        return self.name