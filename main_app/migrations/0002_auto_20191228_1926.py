# Generated by Django 3.0 on 2019-12-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='baths',
            field=models.FloatField(),
        ),
    ]
