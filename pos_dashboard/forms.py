from django import forms
from userapp.models import User,Profile
from email.policy import default
from store.models import *
from .models import *
from paymentApp.models import *
from django.forms import inlineformset_factory
from django.utils import timezone
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from userapp.models import User,Profile
from django.forms import ModelChoiceField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'


class SupplierAddForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "supplier_type", "supplier_ID", "address", "phone", "email", "start_date",
        "amount", "guarantor_name","guarantor_phone","Chassis_no","Transport_name","image"]


class Product_Add_Form(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"


class Purchase_Product_Form(forms.Form):
    class Meta:
        model = Purchase_Product
        fields = "__all__"


class Sales_Product_Form(forms.ModelForm):
    class Meta:
        model = Sales_Product
        fields = ["customer_name", "phone", "billing_date","sale_product_name","product_code",
        "category","brand","quantity","unit","unit_price",
        "sale_price","total_price","total_descount","sub_total","paid","due"]


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields =['category_name','parent','img']

 
class BrandAddForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields =['name','image']


class UnitAddForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields =['name']