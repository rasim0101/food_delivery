from django.contrib import admin
from .models import *
from slugify import slugify


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['title']
	prepopulated_fields = { 'slug': ['title'],}


class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'category')
	prepopulated_fields = { 'slug': ['name'],}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
