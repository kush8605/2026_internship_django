"""
URL configuration for learning26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include
# from views import test
#localhost:8000/test/
urlpatterns = [
    path('admin/', admin.site.urls),
    path("test/",views.test),
    path("about/",views.AboutUs),
    path("contact/",views.contactUs),
    path("",views.home),
    path("movies/",views.movies),
    path("shows/",views.shows),
    path("news/",views.news),
    path("recipe/",views.recipe),
    path("team/",views.team),
    path("moviessuggest/",views.moviessuggest),

    path("student/", include('student.urls')),
   
 

]