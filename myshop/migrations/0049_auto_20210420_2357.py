# Generated by Django 3.1.7 on 2021-04-20 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0048_auto_20210419_1241'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together={('language_code', 'master')},
        ),
    ]
