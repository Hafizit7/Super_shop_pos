# Generated by Django 3.2.15 on 2022-10-23 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_alter_product_sort_discription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_paid_amount',
        ),
    ]
