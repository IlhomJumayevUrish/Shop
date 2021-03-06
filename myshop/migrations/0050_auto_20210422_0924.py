# Generated by Django 3.1.7 on 2021-04-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0049_auto_20210420_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Savat', 'verbose_name_plural': 'Savatlar'},
        ),
        migrations.AlterModelOptions(
            name='cartproduct',
            options={'ordering': ['-id'], 'verbose_name': 'Savat tavar'},
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=45, verbose_name='Email'),
        ),
        migrations.AlterUniqueTogether(
            name='categorystranslation',
            unique_together={('language_code', 'master')},
        ),
        migrations.AlterUniqueTogether(
            name='rangtranslation',
            unique_together={('language_code', 'master')},
        ),
        migrations.AlterUniqueTogether(
            name='subcategorystranslation',
            unique_together={('language_code', 'master')},
        ),
    ]
