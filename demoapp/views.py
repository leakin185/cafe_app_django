from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from demoapp.forms import ReservationForm

# Create your views here.
# def index(request): 
#     return HttpResponse("Hello, world. This is the index view of Demoapp.") 

def form_view(request): 
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid(): 
            form.save()
    context = {"form":form}
    return render(request, "home.html", context)

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 

def home(request): 
    return HttpResponse("Welcome to Little Lemon!")

def display_date(request): 
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)

def about(request): 
    return HttpResponse("About us")

def menu(request): 
    return HttpResponse("Menu for Little Lemon")

def book(request): 
    return HttpResponse("Make a booking")