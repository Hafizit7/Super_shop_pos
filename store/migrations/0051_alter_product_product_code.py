# Generated by Django 3.2.15 on 2022-11-17 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0050_alter_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(max_length=150),
        ),
    ]