# Generated by Django 3.1.7 on 2021-04-11 07:57

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='basket',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
