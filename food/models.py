from django.db import models

def product_photo_dir(instance, filename):
	return 'product_photos/'+instance.id + '/' + filename

def category_photo_dir(instance, filename):
	return 'category_photos/'+instance.id + '/' + filename


class Category(models.Model):
	name = models.CharField(max_length=15)
	photo = models.ImageField(upload_to='category_photos', default='default.jpg')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name="Категория"
		verbose_name_plural="Категории" 




class Product(models.Model):
	# BURGERS = 'burgers'
	# SALADS = 'salads'
	# SNACKS = 'snacks'
	# POTATOES = 'potatoes'
	# SOUPS = 'soups'
	# SAUCES = 'sauces'
	# BEVERAGES = 'beverages'
	# CATEGORIES = (
	# 	('BURGERS', 'Burgers'),
	# 	('SALADS', 'Salads'),
	# 	('SNACKS', 'Snacks'),
	# 	('POTATOES', 'Potatoes'),
	# 	('SOUPS', 'Soups'),
	# 	('SAUCES', 'Sauces'),
	# 	('BEVERAGES', 'Beverages')
	# )
	name = models.CharField(max_length=50, verbose_name="Title")
	price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
	description = models.TextField(verbose_name="Description")
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	# category = models.CharField(max_length=10, choices=CATEGORIES, default=BURGERS, verbose_name="Category")
	product_photo = models.ImageField(upload_to='product_photos', default='default.jpg')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name="Товар"
		verbose_name_plural="Товары" 

