# Generated by Django 4.0.4 on 2022-06-19 07:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 19, 7, 23, 49, 497194, tzinfo=utc)),
        ),
    ]
