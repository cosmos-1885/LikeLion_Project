# Generated by Django 4.1 on 2022-08-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='place',
            field=models.TextField(null=True, verbose_name='수령 장소'),
        ),
    ]
