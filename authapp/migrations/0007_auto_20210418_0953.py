# Generated by Django 3.1.7 on 2021-04-18 06:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210411_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 20, 6, 53, 11, 360295, tzinfo=utc)),
        ),
    ]
