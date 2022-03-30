# Generated by Django 4.0.3 on 2022-03-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_remove_category_slug_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
    ]
