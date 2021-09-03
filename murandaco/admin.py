from django.contrib import admin
from .models import Carousel, Gallery, Product, Category, Comment, Order, OrderItem, Payment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Gallery)
admin.site.register(Carousel)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Carousel)
# admin.site.register(Carousel)

# Register your models here.
