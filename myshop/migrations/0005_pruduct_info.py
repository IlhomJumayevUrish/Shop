# Generated by Django 3.1.7 on 2021-03-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_pruduct_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='pruduct',
            name='info',
            field=models.CharField(blank=True, max_length=50, verbose_name='Qisqa malumot'),
        ),
    ]
