from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.forms import modelform_factory
from django.urls import reverse
from product.forms import ProductForm
from product.models import Product


def create_few(request):
    ProductFormSet = modelformset_factory(
        model=Product,
        form=ProductForm,
        extra=2
    )
    context = {}

    if request.method == "POST":
        formset = ProductFormSet(request.POST. request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect(reverse("home"))
    
    context["formset"] = ProductFormSet(queryset=Product.objects.none)
    return render(request, "product/create_few.html", context)
