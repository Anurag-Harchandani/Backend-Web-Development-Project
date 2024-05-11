from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('bill', views.bill, name='bill'),
]
