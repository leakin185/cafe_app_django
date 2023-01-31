from django.contrib import admin
from .models import MenuCategory
from .models import Menu, Drink, DrinkCategory
from .models import Reservation
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User 
from .models import Person 

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(DrinkCategory)
admin.site.register(Drink)
admin.site.register(Reservation)

# Unregister the provided model admin:  
admin.site.unregister(User) 

@admin.register(User) 
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ] 

    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form 