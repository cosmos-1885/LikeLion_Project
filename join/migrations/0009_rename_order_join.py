# Generated by Django 4.1 on 2022-08-09 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_people'),
        ('users', '0004_remove_users_level_users_address_users_name_and_more'),
        ('join', '0008_remove_order_quantity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Join',
        ),
    ]
