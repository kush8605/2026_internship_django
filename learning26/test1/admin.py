from django.contrib import admin
from .models import User,Car,Inquiry,Message,CarImage,TestDrive,review

# Register your models here.
admin.site.register(User)
admin.site.register(Car)
admin.site.register(Inquiry)
admin.site.register(Message)
admin.site.register(CarImage)
admin.site.register(TestDrive)
admin.site.register(review)

