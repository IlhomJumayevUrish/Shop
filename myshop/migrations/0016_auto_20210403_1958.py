# Generated by Django 3.1.7 on 2021-04-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0015_auto_20210403_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Bolglar'},
        ),
        migrations.AddField(
            model_name='blog',
            name='vaqt',
            field=models.DateField(auto_now=True, verbose_name='Vaqt'),
        ),
    ]
