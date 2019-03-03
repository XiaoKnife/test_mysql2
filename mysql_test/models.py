from django.db import models

# Create your models here.
class minitest(models.Model):
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)

class userinfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()