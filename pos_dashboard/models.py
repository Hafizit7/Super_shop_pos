from django.db import models
from store.models import *
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='media/Category_image')

    class Meta:
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        
        return self.category_name

class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    discription = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='media/Brand_image')

    class Meta:
        
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'

    def __str__(self):
        
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    supplier_type = models.CharField(max_length=100)
    supplier_ID = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    start_date = models.DateField(max_length=50)
    amount = models.FloatField(max_length=30)
    guarantor_name = models.CharField(max_length=100)
    guarantor_phone = models.IntegerField()
    Chassis_no = models.CharField(max_length=30)
    Transport_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='media/supplier_image')
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    class Meta:
   
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
    def __str__(self):

        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    customer_ID = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    start_date = models.DateField(max_length=50)
    image = models.ImageField(upload_to ='media/supplier_image')
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    class Meta:
   
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'
    def __str__(self):

        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        
        return self.name


class Purchase_Product(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    billing_date = models.DateField()
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_code = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    buy_price = models.FloatField()
    sale_price = models.FloatField()
    whole_sale_price = models.FloatField()
    total_price = models.FloatField()
    total_descount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField()
    paid = models.FloatField()
    due = models.FloatField( blank=True, null=True)
    image = models.ImageField(upload_to='media/')
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    unit = models.ForeignKey("pos_dashboard.Unit", related_name="unit", blank=True, null=True, on_delete=models.CASCADE)
    supplier_name = models.ForeignKey(Supplier, related_name="purchase_Product", blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey("pos_dashboard.Category", related_name="category", blank=True, null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey("pos_dashboard.Brand", related_name="brand", blank=True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        
        verbose_name = 'Purchase_Product'
        verbose_name_plural = 'Purchase_Products'

    def __str__(self):
            
        return self.product_name

class Sales_Product(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    billing_date = models.DateField()
    product_code = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField()
    sale_price = models.FloatField()
    total_price = models.FloatField()
    total_descount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField()
    paid = models.FloatField()
    due = models.FloatField(blank=True, null=True)
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    sale_product_name = models.ForeignKey(Purchase_Product, blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Sales_Product'
        verbose_name_plural = 'Sales_Products'

    def __str__(self):
        return self.sale_product_name.product_name

    def save(self, *args, **kwargs):
        if self.sale_product_name:
            self.product_code = self.sale_product_name.product_code
            self.unit_price = self.sale_product_name.unit_price
        super().save(*args, **kwargs)


class return_purchase(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)

    # TODO: Define fields here

    class Meta:

        verbose_name = 'return_purchase'
        verbose_name_plural = 'return_purchases'

    def __str__(self):
        return self.name
