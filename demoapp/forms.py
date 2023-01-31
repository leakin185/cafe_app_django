from django import forms 
from django.forms.widgets import NumberInput

FAVORITE_DISH = [ 
    ('italian', 'Italian'), 
    ('greek', 'Greek'), 
    ('turkish', 'Turkish')
]

class DemoForm(forms.Form): 
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), label="Enter Email Address", required=False)
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}), required=False, help_text="Enter the exact date")
    favourite_dish = forms.ChoiceField(choices=FAVORITE_DISH, required=False)