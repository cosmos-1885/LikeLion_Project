# Generated by Django 4.1 on 2022-08-08 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_buy_link_product_place_product_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]