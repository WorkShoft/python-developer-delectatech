# Generated by Django 3.0.7 on 2020-06-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20200628_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='segments',
            field=models.ManyToManyField(related_name='restaurants', to='restaurants.Segment'),
        ),
    ]
