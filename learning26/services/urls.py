from . import views
from django.urls import path

urlpatterns = [
   path('servicelist/', views.servicelist, name='servicelist'),
   path('serviceform/', views.serviceform, name='serviceform'),
   path('deleteservice/<int:id>/', views.deleteservice, name='deleteservice'),
   path('updateservice/<int:id>/', views.updateservice, name='updateservice'),
   path('sortservice/<int:id>/', views.sortservice, name='sortservice'),
]