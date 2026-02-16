from django import forms
from . models import Course, Employee, instagram, search


# employee form 
# model form -->it will create form using model fileds
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"   # it will create form for all fields of model


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"      


class InstagramForm(forms.ModelForm):
    class Meta:
        model = instagram
        fields = "__all__"          

class SearchForm(forms.ModelForm):
    class Meta:
        model = search
        fields = ['name','age']    


              