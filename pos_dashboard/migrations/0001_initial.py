# Generated by Django 3.2.15 on 2023-07-11 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='brandImg')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='CategoryImg')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pos_dashboard.category')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('customer_ID', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('start_date', models.DateField(max_length=50)),
                ('image', models.ImageField(upload_to='media/supplier_image')),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Purchase_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('billing_date', models.DateField()),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_code', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('buy_price', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('whole_sale_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('total_descount', models.FloatField(blank=True, null=True)),
                ('sub_total', models.FloatField()),
                ('paid', models.FloatField()),
                ('due', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='media/')),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='pos_dashboard.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='pos_dashboard.category')),
            ],
            options={
                'verbose_name': 'Purchase_Product',
                'verbose_name_plural': 'Purchase_Products',
            },
        ),
        migrations.CreateModel(
            name='return_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'return_purchase',
                'verbose_name_plural': 'return_purchases',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('supplier_type', models.CharField(max_length=100)),
                ('supplier_ID', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('start_date', models.DateField(max_length=50)),
                ('amount', models.FloatField(max_length=30)),
                ('guarantor_name', models.CharField(max_length=100)),
                ('guarantor_phone', models.IntegerField()),
                ('Chassis_no', models.CharField(max_length=30)),
                ('Transport_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/supplier_image')),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='Sales_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('billing_date', models.DateField()),
                ('product_code', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('unit_price', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('total_descount', models.FloatField(blank=True, null=True)),
                ('sub_total', models.FloatField()),
                ('paid', models.FloatField()),
                ('due', models.FloatField(blank=True, null=True)),
                ('Created_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('Updated_at', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.category')),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.customer')),
                ('sale_product_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.purchase_product')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.unit')),
            ],
            options={
                'verbose_name': 'Sales_Product',
                'verbose_name_plural': 'Sales_Products',
            },
        ),
        migrations.AddField(
            model_name='purchase_product',
            name='supplier_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase_Product', to='pos_dashboard.supplier'),
        ),
        migrations.AddField(
            model_name='purchase_product',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit', to='pos_dashboard.unit'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_code', models.CharField(blank=True, max_length=100, null=True)),
                ('product_details', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos_dashboard.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
