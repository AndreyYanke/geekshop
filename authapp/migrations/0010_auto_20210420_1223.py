# Generated by Django 3.1.7 on 2021-04-20 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20210418_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 9, 23, 41, 463679, tzinfo=utc)),
        ),
    ]
