from django.urls import path
from . import views

urlpatterns = [
   path('employeelist/', views.employeelist),
    path('employeeFilter/', views.employeeFilter),


]
