from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
	return render(request, 'food/index.html')

def categories(request):
	categories = Category.objects.all()
	context = {
		'categories': categories
	}
	return render(request, 'food/categories.html', context)


def product_list(request, category_id):
	product_list = Product.objects.filter(category=category_id)
	context = {
		'product_list': product_list,
		'category_id': category_id
	}
	return render(request, 'food/product_list.html', context)


def product(request, category_id, product_id):
	product = get_object_or_404(Product, id=product_id)
	context = {
		'product': product
	}
	return render(request, 'food/product.html', context)
	
