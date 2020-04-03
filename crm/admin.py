from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','user')
    list_display_links = ('id', 'name')
    search_fields= ('name','phone', 'email')
    list_per_page = 20

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category','description')
    list_display_links = ('id', 'name')
    search_fields= ('name',)
    list_per_page = 20

class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id', 'name')
    search_fields= ('name',)
    list_per_page = 20

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 'product', 'status', 'note')
    list_display_links = ('id', 'product')
    list_editable = ('status',)
    search_fields= ('product',)
    list_per_page = 20


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order, OrderAdmin)