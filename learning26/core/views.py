from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from django.contrib.auth import login
# Create your views here.
def registerUser(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #is_staff = true
            form.save()
            return redirect('employeeList')
    else:
        form = UserForm()
        return render(request,'core/register.html',{'form':form})