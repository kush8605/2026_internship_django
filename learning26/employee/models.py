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
