# Generated by Django 3.2.15 on 2022-11-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0069_remove_productpercel_tracking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpercel',
            name='tracking_id',
            field=models.CharField(default='fbsuerhfdes', max_length=150),
        ),
        migrations.AlterField(
            model_name='productpercel',
            name='cash_collection_amount',
            field=models.CharField(default='500', max_length=150),
        ),
    ]