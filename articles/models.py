from django.db import models
from datetime import datetime
from team.models import Team

# Create your models here.
class Article(models.Model):
    TITLE =(
    ("International", "international"),
    ("Education", "education"),
    ("Sport", "sport"),
    ("Local", "local"),
    ("Entertainment", "entertainment"),
    )
    reporter= models.ForeignKey(Team, on_delete= models.DO_NOTHING)
    topic= models.CharField(max_length=200)
    title= models.CharField(choices =TITLE, max_length=15,default= 'draft')
    description= models.TextField()
    description2= models.TextField(blank=True)
    post_date= models.DateTimeField(default=datetime.now, blank= True)
    photo_main= models.ImageField(upload_to= 'photos/%Y/%m/%d/', blank=True)
    photo_1= models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    video= models.TextField( blank=True,)
    video1= models.TextField(blank=True)
    is_published= models.BooleanField(default=True)
    def __str__(self):
        return self.topic
