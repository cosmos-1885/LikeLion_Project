# Generated by Django 4.1 on 2022-08-08 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
    ]
