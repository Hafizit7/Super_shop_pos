# Generated by Django 3.2.15 on 2023-07-11 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.unit'),
        ),
    ]
