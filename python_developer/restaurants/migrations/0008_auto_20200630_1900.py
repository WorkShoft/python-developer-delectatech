# Generated by Django 3.0.7 on 2020-06-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_remove_segment_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='average_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='total_reviews',
            field=models.IntegerField(null=True),
        ),
    ]