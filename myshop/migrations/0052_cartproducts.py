# Generated by Django 3.1.7 on 2021-05-08 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0051_auto_20210507_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Jami summa')),
                ('qty', models.PositiveIntegerField(default=0, verbose_name='Jami soni')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.product', verbose_name='Tavar')),
            ],
            options={
                'verbose_name': 'Savat tavar',
                'ordering': ['-id'],
            },
        ),
    ]
