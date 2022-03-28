from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
	return render(request, 'food/index.html')

def product(request, slug):
	product = get_object_or_404(Product, slug=slug)
	context = {
		'product': product
	}
	return render(request, 'food/product.html', context)
	