from django.urls import path
from . import views

app_name= 'orders'

urlpatterns = [
    path('create/', views.order_cart , name='order_cart'),
]
