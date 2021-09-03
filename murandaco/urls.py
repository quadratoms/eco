from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cat/<int:pk>', views.category),
    path('product/<int:pk>', views.product),
    path('cart', views.cart),
    path('verify/<str:pk>', views.verify_payment),
    path('addto/<int:id>', views.add_to_cart),
    path('remove/<int:id>', views.remove_from_cart),
    path('singleremove/<int:id>', views.remove_single_item_from_cart),
]
