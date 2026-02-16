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

def recipe(request):
    ingredient = ["water","salt"]
    data = {"name": "maggie", "time": 1, "ingredients": ingredient}
    return render(request,"recipe.html",data)

def team(request):
    playerlist = ["Virat Kohli","AB de Villiers","Yuzvendra Chahal","Devdutt Padikkal","Chris Gayle","Glenn Maxwell","Mohammed Siraj","KL Rahul","salt","watson","hazlewood"]
    data1 = {"teamname" : "RCB", "trophy" : 1, "captain" : "Virat Kohli","playerlists": playerlist}
    return render(request,"team.html",data1)

def moviessuggest(request):
    thriller = ["Inception","The Dark Knight","Interstellar","The Prestige","Memento"]
    comedy = ["The Hangover","Superbad","Step Brothers","Anchorman","Bridesmaids"]
    crime = ["Se7en","The Godfather","Pulp Fiction","Gone Girl","Zodiac"]
    data2 = {"Thriller": thriller, "Comedy": comedy, "Crime": crime}
    return render(request,"moviessuggest.html", data2)




        