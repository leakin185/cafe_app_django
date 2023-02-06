from django.urls import path 
from . import views 
from .views import NewView 

urlpatterns = [ 
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('date', views.display_date, name='date'), 
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('menu_card/', views.menu_by_id),
    path('', views.home, name='home'), 
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'),
    path('aboutNew/', NewView.as_view()),   
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]