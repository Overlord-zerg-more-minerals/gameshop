from django.shortcuts import render, redirect
from product.models import *
from product.forms import ProductForm


def products(request):
    context = {}
    context["products"] = Product.objects.filter(availability=True)
    return render(request, "product/products.html", context)


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


def create_product(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context["products"] = Product.objects.filter(availability=True)
            context["message"] = "Товар добавлен"
            return render(request, "product/products.html", context)

    
    context["form"] = ProductForm()
    
    return render(
        request,
        "product/test_form.html",
        context    
    )
    

def edit_product(request, id):
    product = Product.objects.get(id=id)
    context = {}

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context["products"] = Product.objects.filter(availability=True)
            context["message"] = "Изменено"
            return render(request, "product/products.html", context)

    
    
    context["form"] = ProductForm(instance=product)
    
    return render(
        request,
        "product/test_form.html",
        context    
    )