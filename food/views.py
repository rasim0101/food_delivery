from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
	return render(request, 'food/index.html')

def category(request):
	category = Category.objects.all()
	context = {
		'category': category
	}
	return render(request, 'food/category.html', context)


def product_list(request, slug):
	product_list = get_object_or_404(Category, slug=slug)
	context = {
		'product_list': product_list
	}
	return render(request, 'food/product_list.html', context)


def product(request, slug):
	product = get_object_or_404(Product, slug=slug)
	context = {
		'product': product
	}
	return render(request, 'food/product.html', context)
	
