from django.urls import path
from . import views

urlpatterns = [
 
   path("marks/",views.studentmarks),
   path("details/",views.studentdetails),
   path("subjects/",views.studentsubjects),
   path("servicelist/",views.servicelist, name="service_list"),
   path("createservice/",views.createService, name="create_service"),
   path("deleteservice/<int:id>/",views.deleteservice, name="delete_service"),
]
