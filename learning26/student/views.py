from django.shortcuts import render

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
