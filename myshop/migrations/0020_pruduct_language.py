# Generated by Django 3.1.7 on 2021-04-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0019_auto_20210405_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='pruduct',
            name='language',
            field=models.CharField(blank=True, choices=[('uz', 'uz'), ('en', 'en')], max_length=20),
        ),
    ]
