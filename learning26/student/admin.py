from django.contrib import admin
from .models import student,product,car,StudentProfile,Category,Service,department,hod_details,Author,Book,Hospital,Doctor,Movie,Actor,Post,Comment

# Register your models here.
admin.site.register(student)
admin.site.register(product)
admin.site.register(car)
admin.site.register(department)
admin.site.register(hod_details)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Post)
admin.site.register(Comment)

