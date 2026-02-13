from django.http import HttpResponse
from django.shortcuts import render, HttpResponse,redirect
from . models import Employee
from . forms import EmployeeForm,CourseForm,InstagramForm,SearchForm



# Create your views here.
def employeelist(request):
    employees = Employee.objects.all().values()
    print(employees)
    return render(request, 'employee/employee_list.html', {'employees': employees})



def employeeFilter(request):
    #where select  from employee where name = "kush"
    employee1 = Employee.objects.filter(name ="kush").values()
    # #selet  from employee where post = "Developer"
    employee2 = Employee.objects.filter(post ="Developer").values()
    # #select  from employee where name = "kush" and post = "Developer"
    employee3 = Employee.objects.filter(name ="kush",post ="Developer").values()
   
    # #select  from employee where age > 25
    # employee4 = Employee.objects.filter(age>25).values()
    employee4 = Employee.objects.filter(age__gt=25).values()
    employee5 = Employee.objects.filter(age__gte=25).values()

    # #lt , lte
    employee19 = Employee.objects.filter(age__lt=30).values()
    employee20 = Employee.objects.filter(age__lte=30).values()


    # #string queries
    # exact for post or any thing like name
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    employee7 = Employee.objects.filter(post__iexact="developer").values()

    # #contains
    employee8 = Employee.objects.filter(name__contains="N").values()
    employee9 = Employee.objects.filter(name__icontains="n").values()

    # #startswith endswith
    employee10 = Employee.objects.filter(name__startswith="D").values()
    employee11 = Employee.objects.filter(name__iendswith="H").values()
    employee12 = Employee.objects.filter(name__istartswith="d").values()
    employee13 = Employee.objects.filter(name__iendswith="H").values()

    # #in
    employee14 = Employee.objects.filter(name__in=["kush","Nigam"]).values()    

    # #range
    employee15 = Employee.objects.filter(age__range=[28,30]).values()    

    # #order by
    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc

    employee18 = Employee.objects.order_by("-salary").values()    #desc

    

    #and
    print("query 1",employee1)
    print("query 2",employee2)
    print("query 3",employee3)
    print("query 4",employee4)
    print("query 5",employee5)
    print("query 6",employee6)   
    print("query 7",employee7) 
    print("query 8",employee8) 
    print("query 9",employee9) 
    print("query 10",employee10) 
    print("query 11",employee11) 
    print("query 12",employee12) 
    print("query 13",employee13) 
    print("query 14",employee14) 
    print("query 15",employee15) 
    print("query 16",employee16) 
    print("query 17",employee17) 
    print("query 18",employee18)
    print("query 19",employee19) 
    print("query 20",employee20)
    return render(request, 'employee/employeeFilter.html')



def createemployee(request):
     Employee.objects.create(name="ajay",age=23,salary=23000,post="HR",join_date="2022-01-01")
     return HttpResponse("EMPLOYEE CREATED...")




def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save() #it same as create
        # return HttpResponse("EMPLOYEE CREATED...")
        return redirect("employeeList")
    else:
        #form object create --> html
        form = EmployeeForm() #form object        
        return render(request,"employee/createEmployeeForm.html",{"form":form})
    

def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        form.save() #it same as create
        return HttpResponse("Course CREATED...")     
    else:
        form = CourseForm() #form object        
        return render(request,"employee/createCourse.html",{"form":form})


def createInstagram(request):
    if request.method == "POST":
        form = InstagramForm(request.POST)
        form.save() #it same as create
        return HttpResponse("Instagram CREATED...")    
    else:
        form = InstagramForm() #form object        
        return render(request,"employee/createInstagram.html",{"form":form})  


def createSearch(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        form.save() #it same as create
        return HttpResponse("Search CREATED...")    
    else:
        form = SearchForm() #form object        
        return render(request,"employee/createSearch.html",{"form":form})     
    


def deleteEmployee(request,id):
    #delete from employees where id = 1
    print("id from url = ",id)
    Employee.objects.filter(id=id).delete()
    # return HttpResponse("EMPLOYEE DELETED...")  
    return redirect("employeeList") #url --> name -->

def filterEmployee(request):
    print("filter employee called...")
    employees = Employee.objects.filter(age__gte=25).values()
    print("filter employees = ",employees)
    #return redirect("employeeList")
    return render(request,"employee/employee_list.html",{"employees":employees})

def sortemployees(request,id):
    if id == 1:
       employees = Employee.objects.all().order_by("age").values
    elif id == 2:
       employees = Employee.objects.all().order_by("-age").values

    return render(request, "employee/employee_list.html",{"employees":employees})
