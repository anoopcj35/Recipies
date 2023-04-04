from django.db import models




class Recipe(models.Model):
    recipename=models.CharField(max_length=40)
    recipeingredients=models.CharField(max_length=50)
    recipeprice=models.IntegerField()
    image=models.ImageField(upload_to='sample',default='null.jpg')


class Category(models.Model):
    categoryname=models.CharField(max_length=40)
    categoryimage=models.ImageField(upload_to='category')


class Product(models.Model):
    productname=models.CharField(max_length=67)
    productprice=models.IntegerField()
    productimage=models.ImageField(upload_to='product')   
    category=models.CharField(max_length=89) 