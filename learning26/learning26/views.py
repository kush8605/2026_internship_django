from django.shortcuts import render
from django.http import HttpResponse

#specific url
def test(request):
    return HttpResponse("hello")


def AboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def movies(request):
    return render(request,"movies.html")

def shows(request):
    return render(request,"shows.html")

def news(request):
    return render(request,"news.html")