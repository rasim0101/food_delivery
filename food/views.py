from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

def index(request):
	categories = Category.objects.prefetch_related('product_set').all()
	context = {
		'categories': categories
	}
	return render(request, 'food/index.html', context)

def categories(request):
	categories = Category.objects.all()
	context = {
		'categories': categories
	}
	return render(request, 'food/categories.html', context)


def product_list(request, slug):
	category = get_object_or_404(Category, slug=slug)
	products = Category.objects.get(slug=slug).product_set.all()
	context = {
		'products': products,
		'category': category,
	}
	return render(request, 'food/product_list.html', context)


def product(request, category_slug, product_slug):
	product = get_object_or_404(Product, slug=product_slug)
	category = get_object_or_404(Category, slug=category_slug)
	similar_products = Category.objects.get(slug=category_slug).product_set.filter(~Q(slug=product_slug))
	context = {
		'product': product,
		'category': category,
    	'similar_products': similar_products,
	}
	return render(request, 'food/product.html', context)
	
