# Generated by Django 3.1.7 on 2021-04-19 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0038_yangiliklar_yangiliklartranslation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yangiliklar',
            name='image',
        ),
    ]