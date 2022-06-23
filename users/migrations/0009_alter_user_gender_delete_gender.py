# Generated by Django 4.0.4 on 2022-06-19 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_gender_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]
