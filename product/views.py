from django.shortcuts import render
from product.models import *


def products(request):
    context = {}
    context["products"] = Product.objects.filter(availability=True)
    return render(request, "product/products.html", context)
