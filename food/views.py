from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
	collection = Category.objects.all().select_related('product')
	context = {
		'collection': collection,
		'product': product
	}
	return render(request, 'food/index.html', context)

def categories(request):
	categories = Category.objects.all()
	context = {
		'categories': categories
	}
	return render(request, 'food/categories.html', context)


def product_list(request, category_slug):
	product_list = Product.objects.all()
	context = {
		'product_list': product_list,
		'category_slug': category_slug
	}
	return render(request, 'food/product_list.html', context)


def product(request, category_slug, product_slug):
	product = get_object_or_404(Product, slug=product_slug)
	context = {
		'product': product,

	}
	return render(request, 'food/product.html', context)
	
