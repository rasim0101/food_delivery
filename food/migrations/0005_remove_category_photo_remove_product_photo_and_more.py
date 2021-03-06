# Generated by Django 4.0.3 on 2022-03-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_category_options_category_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.AddField(
            model_name='category',
            name='category_photo',
            field=models.ImageField(default='default.jpg', upload_to='category_image_upload'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_photo',
            field=models.ImageField(default='default.jpg', upload_to='product_image_upload'),
        ),
    ]
