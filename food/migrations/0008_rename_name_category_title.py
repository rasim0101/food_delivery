# Generated by Django 4.0.3 on 2022-03-28 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]