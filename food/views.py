from django.shortcuts import render
from .models import Product, Category

def index(request):
	return render(request, 'food/index.html')

def product(request, id):
	product = Product.objects.get(id=id)
	context = {
		'product': product
	}
	return render(request, 'food/product.html', context)
	