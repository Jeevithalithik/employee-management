from django.db import models

# Create your models here.

class program(models.Model):
    eid=models.IntegerField()
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.BigIntegerField() 
    email=models.EmailField()
    date=models.DateField()
    position=models.CharField(max_length=50)
    salary=models.IntegerField()