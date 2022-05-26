from django.db import models

# Create your models here.

class CarrerUsers(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    # profile_pic = models.ImageField(upload_to='pics')
    age = models.CharField(max_length=200)
