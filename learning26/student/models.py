from django.db import models

# Create your models here.
class student(models.Model):
    studentname=models.CharField(max_length=100)
    studentage=models.IntegerField()
    studentcity=models.CharField(max_length=100)
    studentemail=models.EmailField(null=True)

    # meta class
    class Meta:
        db_table="student"

class product(models.Model):
    productname=models.CharField(max_length=100)
    productprice=models.IntegerField()
    productdescription=models.TextField(max_length=100)
    productstock=models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table="product"     

class car(models.Model):
    carname=models.CharField(max_length=100)
    carmodel=models.CharField(max_length=100)
    carprice=models.PositiveIntegerField()

    class Meta:
        db_table="car"
