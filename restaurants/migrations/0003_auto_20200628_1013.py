# Generated by Django 3.0.7 on 2020-06-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0002_auto_20200628_1008"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="street_address",
            field=models.TextField(null=True),
        ),
    ]