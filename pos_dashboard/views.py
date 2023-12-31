from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from store.models import *
from userapp.models import User
from userapp.forms import *
from store.forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect

from requests import request
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from userapp.decorators import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from userapp.forms import *
from django.views.generic.detail import DetailView

from django.http import JsonResponse

# Create your views here.

@login_required
def index(request):
    return render(request, 'pos_dashboard/index.html')


#User

@login_required
# @daseboard_required
def user_list(request):
    user=User.objects.all()
    context={
        'user':user
    }
    return render(request, 'pos_dashboard/user/userlist.html', context)


@login_required
# @daseboard_required
def user_add(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add')
            return redirect('user_list')
    else:
        form =RegisterForm()
    return render(request,'pos_dashboard/user/adduser.html',{'form':form})


@login_required
# @daseboard_required
def user_update(request,pk):
    user =get_object_or_404(User,pk=pk)
    form =UserForm(request.POST,instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully update')
            return redirect('user_list')
    else:
        form =UserForm(instance=user)
    context={
        'form':form,
    }
    return render(request, 'pos_dashboard/user/user-add.html',context)

@login_required
# @daseboard_required
def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Successfully delete')
        return redirect('user_list')
    return render (request, 'dashboard/user/user-delete.html',{'user':user})


# Product
def product (request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    unit = Unit.objects.all()
    if request.method == 'POST':
        form = Product_Add_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new Purchas Product')
            return redirect('product_list')
    else:
        form = Product_Add_Form()
        context = {
            'form':form,
            'category':category,
            'brand':brand,
            'unit':unit,
        
        }
    return render(request,'pos_dashboard/add_product.html', context)

def product_list(request):
    product_list = Products.objects.all()
    context = {
        'product_list':product_list
    }
    return render(request,'pos_dashboard/product_list.html', context)

     
# Supplier
def supplier_add(request):
    if request.method == 'POST':

        form=SupplierAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new Purchas Product')
            return redirect('supplierlist')
    else:
        form = SupplierAddForm()
        context = {
            'form':form
        }
    return render(request, 'pos_dashboard/supplier/add_supplier.html', context)


def supplier_list(request):
    supplier_list = Supplier.objects.all()
    context ={
        'supplier_list':supplier_list
    }
    return render(request, 'pos_dashboard/supplier/supplier_list.html', context)




# Category

def category_add(request):
    categorys = Category.objects.all()
    if request.method == 'POST':
        form=CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new category')
            return redirect('category_list')
    else:
        form = CategoryForm()

    context = {
        'categorys': categorys,
        'form':form 
    }
    return render(request,'pos_dashboard/category/category_add.html',context)


def category_list(request):
    category_list = Category.objects.all()
    context ={
        'category_list':category_list
    }
    return render(request, 'pos_dashboard/category/category_list.html', context)

# Brand

def brand_add(request):
    if request.method == 'POST':
        form=BrandAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new brand')
            return redirect('brand_list')
    else:
        form =BrandAddForm()
    context= {
        'form':form,
        
    }
    return render(request,'pos_dashboard/brand/brand_add.html',context)

def brand_list(request):
    brand_list = Brand.objects.all()
    context={
        'brand_list':brand_list
    }
    return render(request,'pos_dashboard/brand/brand_list.html', context)

# Unit 
def unit_add(request):
    unit_list = Unit.objects.all()

    if request.method == 'POST':
        form=UnitAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new Unit')
            return redirect('unit_add')
    else:
        form =UnitAddForm()

    context={
        'unit_list':unit_list,
        'form':form,
    }
    return render(request,'pos_dashboard/unit/unit_add.html',context)

     
# Purchage
def purchase_product(request):
    unit = Unit.objects.all()
    supplier = Supplier.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()

    if request.method == 'POST':

        form=Purchase_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            
            
            messages.success(request,'successfully add your new Purchas Product')
            return redirect('purchase_list')
    else: 
        form = Purchase_Product_Form()
    
    context = {
        'form':form,
        'category':category,
        'unit':unit,
        'supplier':supplier,
        'brand':brand,

    }
    return render(request, 'pos_dashboard/purchase_product/add_purchase.html',context)
 

def purchase_product_list(request):
    purchase_list = Purchase_Product.objects.all()
    context ={
        'purchase_list':purchase_list
    }
    return render(request, 'pos_dashboard/purchase_product/purchase_list.html', context)


def new_purchase_return(request):

    return render(request, 'pos_dashboard/purchase_product/create_purchase_return.html')


def purchase_return_list(request):
    return render(request, 'pos_dashboard/purchase_product/purchase_return_list.html')

def purchase_due_list(request):

    due_purchase_list = Purchase_Product.objects.filter(due__gt=0)
    context ={
        'due_purchase_list':due_purchase_list
    }
    return render(request, 'pos_dashboard/purchase_product/due_purchase_list.html', context)


from django.http import JsonResponse

def sales_product(request):

    sale_product_name = Purchase_Product.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    customer = Customer.objects.all()
    unit = Unit.objects.all()

    if request.method == 'POST':
        form = Sales_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added your new Sales Product')
            return redirect('sales_list')
    else:
        form = Sales_Product_Form()
    
    context = {
        'form': form,
        'sale_product_name': sale_product_name,
        'category': category,
        'brand':brand,
        'customer':customer,
        'unit':unit
    }
    
    return render(request, 'pos_dashboard/sales/add_sales.html', context)



def sales_list(request):
    sales_li = Sales_Product.objects.all()

    context = {
        'sales_li':sales_li
    }
    return render(request, 'pos_dashboard/sales/sales_list.html', context)


def sales_due_list(request):

    due_sales_list = Sales_Product.objects.filter(due__gt=0)
    context ={
        'due_sales_list':due_sales_list
    }
    return render(request, 'pos_dashboard/sales/due_sales_list.html', context)

