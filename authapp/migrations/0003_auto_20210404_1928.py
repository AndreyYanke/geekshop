# Generated by Django 3.1.7 on 2021-04-04 16:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210404_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 16, 28, 52, 869120, tzinfo=utc)),
        ),
    ]