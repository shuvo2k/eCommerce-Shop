# Generated by Django 2.0.5 on 2018-10-12 13:45

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181012_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='multiple_image',
            field=models.FileField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]