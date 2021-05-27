from django.db import models
from datetime import datetime


# Create your models here.
class Home(models.Model):
    video_link= models.CharField(max_length= 2000)
    create_date= models.DateTimeField(default=datetime.now, blank= True)
    photo= models.ImageField(upload_to= 'photos/%Y/%m/%d/')
    def __str__(self):
        return self.video_link