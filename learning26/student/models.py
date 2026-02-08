from curses import meta
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
        verbose_name_plural="student"

    def __str__(self):
        return self.studentname

class product(models.Model):
    productname=models.CharField(max_length=100)
    productprice=models.IntegerField()
    productdescription=models.TextField(max_length=100)
    productstock=models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table="product" 
        verbose_name_plural="product"    

class car(models.Model):
    carname=models.CharField(max_length=100)
    carmodel=models.CharField(max_length=100)
    carprice=models.PositiveIntegerField()

    class Meta:
        db_table="car"
        verbose_name_plural="car"
    

class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()

    class Meta:
        db_table="studentprofile"
        verbose_name_plural="studentprofile"

    def __str__(self):
     return self.studentId.studentname
        
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"
        verbose_name_plural = "category"

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"
        verbose_name_plural = "service"

    def __str__(self):
        return self.serviceName        


class department(models.Model):
    dept_name = models.CharField(max_length=100)
    building_no = models.CharField(max_length=10)
    established_year = models.IntegerField()

    class Meta:
        db_table = "department"
        verbose_name_plural = "department"

    def __str__(self):
        return self.dept_name

# The One-to-One Model
class hod_details(models.Model):
    # This ensures one department has only one HOD record
    department = models.OneToOneField(department, on_delete=models.CASCADE)
    hod_name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    office_room = models.CharField(max_length=20)

    class Meta:
        db_table = "hod_details"
        verbose_name_plural = "hod_details"

    def __str__(self):
        return f"HOD of {self.department.dept_name}"

    
class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "author"
        verbose_name_plural = "author"

    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField(max_length=100)
    # The 'on_delete' tells Django what to do if the Author is deleted
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')       

    class Meta:
        db_table = "book" 
        verbose_name_plural = "book"  

    def __str__(self):
        return self.title    




class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    class Meta:
        db_table = "hospital" 
        verbose_name_plural = "hospital"  

    def __str__(self):
        return self.name   

        

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    # We put the ForeignKey on the "Many" side (the Doctor)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')  

    class Meta:
        db_table = "doctor"
        verbose_name_plural = "doctor"

    def __str__(self):  
        return f"{self.name} ({self.specialization}) at {self.hospital.name}"    

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        db_table = "actor"
        verbose_name_plural = "actor"

    def __str__(self):
        return self.name    

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    # Many-to-Many can go in either model; here it's in Movie
    cast = models.ManyToManyField(Actor, related_name='movies')

    class Meta:
        db_table = "movie"
        verbose_name_plural = "movie"

    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
     

    class Meta:
        db_table = "post" 
        verbose_name_plural = "post"  

    def __str__(self):
        return self.title

class Comment(models.Model):
    # This links the comment to a specific Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"
        verbose_name_plural = "comment"

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"    