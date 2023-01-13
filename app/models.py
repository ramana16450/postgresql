from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
class student(models.Model):
    name=models.ForeignKey(school,on_delete=models.CASCADE)
    age=models.IntegerField()