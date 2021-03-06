# Generated by Django 3.0.7 on 2020-06-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Segment",
            fields=[
                ("uidentifier", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("size", models.IntegerField()),
                ("average_popularity_rate", models.FloatField(null=True)),
                ("average_satisfaction_rate", models.FloatField(null=True)),
                ("average_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                ("uidentifier", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("street_address", models.TextField()),
                ("longitude", models.DecimalField(decimal_places=7, max_digits=10)),
                ("latitude", models.DecimalField(decimal_places=7, max_digits=10)),
                ("city_name", models.TextField()),
                ("popularity_rate", models.FloatField()),
                ("satisfaction_rate", models.FloatField()),
                ("total_reviews", models.IntegerField()),
                ("average_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("segments", models.ManyToManyField(to="restaurants.Segment")),
            ],
        ),
    ]
