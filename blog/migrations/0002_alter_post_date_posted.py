# Generated by Django 3.2.13 on 2022-07-15 06:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 15, 6, 56, 53, 581970, tzinfo=utc)),
        ),
    ]
