from django.shortcuts import render, redirect
from .forms import ServiceForm
from .models import Service

# Create your views here.

def servicelist(request):
  services = Service.objects.all().order_by('id') 
  print(services)
  return render(request, 'services/servicelist.html', {'services': services})

def serviceform(request):
  print(request.method)
  if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save()
        return redirect("servicelist")
  else:
        form = ServiceForm() #form object        
        return render(request,"services/serviceForm.html",{"form":form})

def deleteservice(request,id):
    print("id from url = ",id)
    Service.objects.filter(id=id).delete()
    return redirect("servicelist") 


def updateservice(request,id):
    service = Service.objects.get(id=id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        form.save()
        return redirect("servicelist")
    else:  
        form = ServiceForm(instance=service) #form object
        return render(request,"services/serviceForm.html",{"form":form})
    
def sortservice(request, id):
  if id == 1:
    services = Service.objects.all().order_by('price')
  elif id == 2:
    services = Service.objects.all().order_by('-price')
  return render(request, 'services/servicelist.html' , {'services': services})

