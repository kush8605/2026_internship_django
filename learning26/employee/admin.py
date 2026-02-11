from django.contrib import admin
from . models import Employee,Course,instagram,search

# Register your models here.
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(instagram)
admin.site.register(search)

