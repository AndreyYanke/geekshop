# Generated by Django 3.1.7 on 2021-04-06 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'элемент заказа', 'verbose_name_plural': 'элементы заказа'},
        ),
    ]
