from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from demoapp.forms import ReservationForm
from .models import Menu
from django.views import View  
from .forms import BookingForm 

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
    return render(request, "about.html")

def menu(request): 
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu_by_id(request): 
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu':newmenu}
    return render(request, "menu_card.html", newmenu_dict)

def home(request): 
    return render(request, "index.html") 

def register(request): 
    return render(request, "register.html", {}) 

def login(request): 
    return render(request, "login.html", {}) 

class NewView(View):   
    def get(self, request):   
        # View logic will place here   
        return HttpResponse('response') 

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 
