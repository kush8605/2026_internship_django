from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    post = models.CharField(max_length=100)
    salary = models.IntegerField()
    join_date = models.DateField()

    class Meta:
        db_table = 'employee_table'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name 


class Course(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        db_table = "course"
    def __str__(self):
        return self.name   



class instagram(models.Model):
    name = models.CharField(max_length=100)
    followers = models.IntegerField()
    following = models.IntegerField()

    class Meta:
        db_table = "instagram"
        verbose_name_plural = "Instagram Accounts"
    def __str__(self):
        return self.name
    
class search(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'search_table'
        verbose_name_plural = 'Searches'

    def __str__(self):
        return self.name  
    


