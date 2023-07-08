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


class ProductForm(forms.ModelForm):
    aditional_discription = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class':'form-control p-20',
        'rows':"4"
    }))
    discription =forms.CharField(widget=CKEditorUploadingWidget(attrs={
        'class':'form-control p-20',
        'rows':"4"
    }))
    flash_sale_add_and_expire_date = forms.DateTimeField(required=False, disabled=False,
                                          widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    
    class Meta:
        model = Product
        fields = '__all__'

class ImageForm(forms.ModelForm):

    class Meta:
        model = ProductImgGallery
        fields = '__all__'


class VariantForm(forms.ModelForm):
    VAR_CATEGORIES = ( 
        ('', '--select variation type--'), 
        ('size', 'size'), 
        ('color', 'color'), 
        )
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
        }))
    category = forms.ChoiceField(choices=VAR_CATEGORIES,widget=forms.Select(attrs={
        'class':'form-control'
        }))
        
    class Meta:
        model = Variation
        fields = '__all__'


VariantFormSet = inlineformset_factory(
    Product, Variation, form=VariantForm,
    extra=1, can_delete=True, can_delete_extra=True
)
ImageFormSet = inlineformset_factory(
    Product, ProductImgGallery, form=ImageForm,
    extra=1, can_delete=True, can_delete_extra=True
)


class SupplierAddForm(forms.ModelForm):
   
    
    class Meta:
        model = Supplier
        fields = ["name", "supplier_type", "supplier_ID", "address", "phone", "email", "start_date",
        "amount", "guarantor_name","guarantor_phone","Chassis_no","Transport_name","image"]


class Purchase_Product_Form(forms.ModelForm):
    class Meta:
        model = Purchase_Product
        fields = "__all__"


class Sales_Product_Form(forms.ModelForm):
    class Meta:
        model = Sales_Product
        fields = ["customer_name", "phone", "billing_date","sale_product_name","product_code",
        "category","brand","quantity","unit","unit_price",
        "sale_price","total_price","total_descount","sub_total","paid","due"]


class CategoryAddForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields =['category_name','parent','image']


class BrandAddForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields =['name','discription','image']


class UnitAddForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields =['name']