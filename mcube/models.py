from django.db import models

# Create your models here.

class Colleges(models.Model):
    college_name = models.CharField(max_length=50)

class Users(models.Model):
    user_first = models.CharField(max_length=20)
    user_last = models.CharField(max_length=20)
    college = models.ForeignKey(Colleges, on_delete=models.CASCADE)

class Scores(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    score = models.IntegerField()

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
