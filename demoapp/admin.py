from django.contrib import admin
from .models import MenuCategory
from .models import Menu, Drink, DrinkCategory
from .models import Reservation

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(DrinkCategory)
admin.site.register(Drink)
admin.site.register(Reservation)