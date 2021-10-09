# Generated by Django 3.1.7 on 2021-04-17 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0024_auto_20210416_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tuman', to='myshop.province', verbose_name='Tuman'),
        ),
        migrations.AlterField(
            model_name='order',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.province', verbose_name='Viloyat'),
        ),
    ]
