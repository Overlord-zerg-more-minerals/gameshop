from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required, \
    user_passes_test
from product.models import *
from product.forms import ProductForm


def products(request):
    context = {}
    if "query" in request.GET:
        word = request.GET.get("query")
        context["products"] = Product.objects.filter(
            Q(availability=True),
            Q(delete=False) |
            Q(title__contains=word) |
            Q(description__contains=word) |
            Q(category__title__contains=word) 
        )

    else:
        context["products"] = Product.objects.filter(
            availability=True,
            delete=False
        )
    return render(request, "product/products.html", context)


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


@login_required(login_url="/personaloffice/")
def create_product(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = request.user
            new_product.save()
            context["products"] = Product.objects.filter(
                availability=True,
                delete=False
            )
            context["message"] = "Товар добавлен"
            return render(request, "product/products.html", context)

    context["form"] = ProductForm()
    
    return render(
        request,
        "product/test_form.html",
        context    
    )
    

@login_required(login_url="/personaloffice/")
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.user != product.user:
        return redirect("home")

    context = {}

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context["products"] = Product.objects.filter(
                availability=True,
                delete=False
            )
            context["message"] = "Изменено"
            return render(request, "product/products.html", context)
    
    context["form"] = ProductForm(instance=product)
    
    return render(
        request,
        "product/test_form.html",
        context    
    )


@login_required(login_url="/personaloffice/")
def delete_product(request, id):
    product = Product.objects.get(id=id)
    context = {}

    if product.user != request.user:
        context["message"] = "Упс, что то пошло не так"
    else:
        product.delete = True
        product.save()
        context["message"] = "Товар был удален"

    context["type"] = "danger"
    return render(request, "core/message.html", context)