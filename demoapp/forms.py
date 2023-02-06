from django import forms 
from django.forms import ModelForm
from .models import Reservation, Booking

class ReservationForm(forms.ModelForm): 
    class Meta: 
        model = Reservation 
        fields = '__all__'

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"