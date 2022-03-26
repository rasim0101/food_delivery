from django.shortcuts import render

def index(request):
	return render(request, 'food/index.html')

def product(request):
	return render(request, 'food/product.html')
	