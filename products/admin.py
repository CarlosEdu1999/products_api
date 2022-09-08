from django.contrib import admin
from products.models import Product


class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'brand', 'description', 'stock', 'active', 'image', 'rating', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category', 'brand')
    list_per_page = 20


admin.site.register(Product, Products)
