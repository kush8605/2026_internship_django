from django.urls import path
from . import views

urlpatterns = [
   path('employeelist/', views.employeelist, name='employeeList'),
   path('employeeFilter/', views.employeeFilter),
   path('createemployee/', views.createemployee),
   path('createEmployeeForm/', views.createEmployeeWithForm, name='employeeForm'),
   path('createCourseForm/', views.createCourse),
   path('createInstagramForm/', views.createInstagram),
   path('createSearchForm/', views.createSearch),
   path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
   path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
   path("sortemployees/<int:id>",views.sortemployees,name="sortEmployee"),
    
]
