from django.db import models
from django.urls import reverse
from slugify import slugify
from ckeditor.fields import RichTextField

def product_image_upload(instance, filename):
	return f"food/{instance.id}/{filename}"


def category_image_upload(instance, filename):
	return f"food/{instance.id}/{filename}"


class Category(models.Model):
	title = models.CharField(max_length=15)
	category_photo = models.ImageField(upload_to='category_image_upload', default='default.jpg')
	slug = models.SlugField(null=True)

	def get_absolute_url(self):
		return reverse('product_list', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		self.slug=slugify(self.title)
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.title

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
	description = RichTextField(null=True, verbose_name="Description")
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	# category = models.CharField(max_length=10, choices=CATEGORIES, default=BURGERS, verbose_name="Category")
	product_photo = models.ImageField(upload_to='product_image_upload', default='default.jpg')
	slug = models.SlugField(null=True)


	def get_absolute_url(self):
		return reverse('product', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		self.slug=slugify(self.name)
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name="Товар"
		verbose_name_plural="Товары" 

