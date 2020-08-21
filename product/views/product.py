from django.shortcuts import render
from django.db.models import Q
from product.models import Product


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


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
