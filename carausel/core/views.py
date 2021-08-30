from typing import ContextManager
from django.shortcuts import render
from .models import *
from product.models import *
# Create your views here.

def HomeView(request):
    obj = Carausel.objects.all()
    products = Product.objects.all()
    products_about=Product.objects.get(id='1')
    products_best_seller=Product.objects.get(id='2')
    products_best_seller1=Product.objects.get(id='3')
    products_best_seller2=Product.objects.get(id='4')

    context = {
        'obj' : obj,
        'products':products,
        'products_about':products_about,
        'products_best_seller':products_best_seller,
        'products_best_seller1':products_best_seller1,
        'products_best_seller2':products_best_seller2,

    }
    return render(request,'home.html',context)

def about(request):
    obj=Carausel.objects.all()
    context = {
        'obj' : obj,
    }
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')