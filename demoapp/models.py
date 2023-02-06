from django.db import models
from django.forms.widgets import NumberInput


# Create your models here.
class MenuCategory(models.Model): 
    menu_category_name = models.CharField(max_length=200)


class DrinkCategory(models.Model): 
    drink_category_name = models.CharField(max_length=200)

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
    
class Drink(models.Model): 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    drink_id = models.ForeignKey(DrinkCategory, on_delete=models.PROTECT, default = None, related_name="category_name")

class Reservation(models.Model): 
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    booking_time = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.first_name

class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 

    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 

class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

