# Generated by Django 3.1.7 on 2021-03-20 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0011_auto_20210320_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.pruduct', verbose_name='images'),
        ),
    ]
