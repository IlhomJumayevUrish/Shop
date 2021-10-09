# Generated by Django 3.1.7 on 2021-04-19 04:34

from django.db import migrations, models
import django.db.models.deletion
import myshop.models
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0037_bloglar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yangiliklar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=myshop.models.image_folder_blog, verbose_name='Image')),
                ('vaqt', models.DateField(auto_now_add=True, verbose_name='Vaqt')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='YangiliklarTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='myshop.yangiliklar')),
            ],
            options={
                'verbose_name': 'yangiliklar Translation',
                'db_table': 'myshop_yangiliklar_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]