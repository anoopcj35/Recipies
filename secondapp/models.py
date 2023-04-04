from django.db import models

# Create your models here.
class Register(models.Model):
    firstname=models.CharField(max_length=34)
    middlename=models.CharField(max_length=45)
    lastname=models.CharField(max_length=56)
    username=models.CharField(max_length=67,)
    password=models.CharField(max_length=72,)
    age=models.IntegerField()
    address=models.CharField(max_length=70)
    phonenumber=models.IntegerField()
    


