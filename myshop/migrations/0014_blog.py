# Generated by Django 3.1.7 on 2021-04-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0013_auto_20210402_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('title', models.TextField(verbose_name='Title')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
        ),
    ]
