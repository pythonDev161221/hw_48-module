from django.contrib import admin

from webapp.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product', 'category', 'price']
    list_filter = ['category']
    search_fields = ['product', 'category']
    fields = ['product', 'price']


admin.site.register(Product, ProductAdmin)
