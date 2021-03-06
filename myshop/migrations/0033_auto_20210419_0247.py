# Generated by Django 3.1.7 on 2021-04-18 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0032_order_orderitem'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='facttranslation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='facttranslation',
            name='master',
        ),
        migrations.AlterModelOptions(
            name='districts',
            options={'verbose_name': 'Tuman', 'verbose_name_plural': 'Tumanlar'},
        ),
        migrations.AlterModelOptions(
            name='districtstranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Tuman Translation'},
        ),
        migrations.AlterModelOptions(
            name='provinces',
            options={'verbose_name': 'Viloyat', 'verbose_name_plural': 'Vloyatlar'},
        ),
        migrations.AlterModelOptions(
            name='provincestranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Viloyat Translation'},
        ),
        migrations.DeleteModel(
            name='Fact',
        ),
        migrations.DeleteModel(
            name='FactTranslation',
        ),
    ]
