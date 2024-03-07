from django.db import models

# Create your models here.

class Movie(models.Model):

    title = models.CharField(max_length=512)
    plot = models.TextField()
    releaese_date = models.DateField()



class Actor(models.Model):
    firs_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    bio = models.TextField()