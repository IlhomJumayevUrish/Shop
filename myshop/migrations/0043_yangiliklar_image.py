# Generated by Django 3.1.7 on 2021-04-19 04:53

from django.db import migrations, models
import myshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0042_auto_20210419_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='yangiliklar',
            name='image',
            field=models.ImageField(default=1, upload_to=myshop.models.image_folder_blog, verbose_name='Image'),
            preserve_default=False,
        ),
    ]