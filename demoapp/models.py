from django.db import models


# Create your models here.
class MenuCategory(models.Model): 
    menu_category_name = models.CharField(max_length=200)


class DrinkCategory(models.Model): 
    drink_category_name = models.CharField(max_length=200)

class Menu(models.Model): 
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name + " : " + self.cuisine
    
class Drink(models.Model): 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    drink_id = models.ForeignKey(DrinkCategory, on_delete=models.PROTECT, default = None, related_name="category_name")

FAVORITE_DISH = [ 
    ('italian', 'Italian'), 
    ('greek', 'Greek'), 
    ('turkish', 'Turkish')
]

class Reservation(models.Model): 
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), label="Enter Email Address", required=False)
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}), required=False, help_text="Enter the exact date")
    favourite_dish = forms.ChoiceField(choices=FAVORITE_DISH, required=False)