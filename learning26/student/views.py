from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm

def studentmarks(request):
    names = {"kush-86", "rahul-90", "ankit-78", "priya-92", "sneha-88"}
    data = {"names": names}
    return render(request, "student/studentmarks.html", data)

def studentdetails(request):
    details = {
        "kush": {"age": 20, "grade": "A"},
        "rahul": {"age": 21, "grade": "B"},
        "ankit": {"age": 19, "grade": "C"},
        "priya": {"age": 22, "grade": "A"},
        "sneha": {"age": 20, "grade": "B"},
    }
    data = {"details": details}
    return render(request, "student/studentdetails.html", data)

def studentsubjects(request):
    subjects = {
        "kush": ["Math", "Science"],
        "rahul": ["English", "History"],
        "ankit": ["Math", "Computer Science"],
        "priya": ["Biology", "Chemistry"],
        "sneha": ["Physics", "Math"],
    }
    
    data = {"subjects": subjects}
    return render(request, "student/studentsubjects.html", data)

def servicelist(request):
    services = Service.objects.all()
    return render(request, "student/servicelist.html", {"services": services})

def createService(request):

    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service_list")
    else:
        form = ServiceForm()
    return render(request, "student/createservice.html", {"form": form})

def deleteservice(request,id):
    print("id from url = ",id)
    Service.objects.filter(id=id).delete()
    return redirect("service_list") 
    