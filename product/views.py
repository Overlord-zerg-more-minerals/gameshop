from django.shortcuts import render, redirect
from django.db.models import Q
from product.models import *
from product.forms import ProductForm


def products(request):
    context = {}
    if "query" in request.GET:
        word = request.GET.get("query")
        context["products"] = Product.objects.filter(
            Q(availability=True),
            Q(title__contains=word) |
            Q(description__contains=word) |
            Q(category__title__contains=word) 
        )

    else:
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