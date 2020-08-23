from django.shortcuts import render
from product.models import Product


def category(request, pk):
    context = {}
    context["products"] = Product.objects.filter(
        category__id=pk,
        availability=True,
        delete=False
    )
    context["category_pk"] = pk
    return render(request, "product/products.html", context)
