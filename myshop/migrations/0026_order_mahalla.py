# Generated by Django 3.1.7 on 2021-04-17 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0025_auto_20210417_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='mahalla',
            field=models.CharField(default=1, max_length=100, verbose_name='Mahalla'),
            preserve_default=False,
        ),
    ]