# Generated by Django 2.0.5 on 2018-10-12 13:30

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181008_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf_image3',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]
