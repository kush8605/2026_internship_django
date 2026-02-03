from django.urls import path
from . import views

urlpatterns = [
 
   path("marks/",views.studentmarks),
   path("details/",views.studentdetails),
    path("subjects/",views.studentsubjects),
]