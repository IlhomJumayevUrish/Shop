# Generated by Django 3.1.7 on 2021-04-17 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0027_auto_20210417_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(blank=True, null=True, verbose_name="To'landi"),
        ),
    ]
