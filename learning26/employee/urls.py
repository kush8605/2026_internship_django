from django.urls import path
from . import views

urlpatterns = [
   path('employeelist/', views.employeelist),
   path('employeeFilter/', views.employeeFilter),
   path('createemployee/', views.createemployee),
   path('createEmployeeForm/', views.createEmployeeWithForm),
   path('createCourseForm/', views.createCourse),
   path('createInstagramForm/', views.createInstagram),
   path('createSearchForm/', views.createSearch),
]
