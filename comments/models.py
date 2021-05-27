from django.db import models
from datetime import datetime


# Create your models here.
class Comment(models.Model):
    article_id= models.IntegerField()
    name= models.CharField(max_length=200)
    phone= models.CharField(max_length=20)
    email= models.EmailField(max_length= 50)
    message= models.TextField()
    comment_date= models.DateTimeField(default=datetime.now, blank= True)
    def __str__(self):
        return self.name