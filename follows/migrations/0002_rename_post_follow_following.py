# Generated by Django 4.0.4 on 2022-07-10 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='post',
            new_name='following',
        ),
    ]
