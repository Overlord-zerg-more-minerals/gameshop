from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Product
from product.forms import ProductForm


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
