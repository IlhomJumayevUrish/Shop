# Generated by Django 3.1.7 on 2021-04-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0026_order_mahalla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(blank=True, verbose_name="To'landi"),
        ),
    ]