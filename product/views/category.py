from django.shortcuts import render
from product.models import Product


def category(request, pk):
    context = {}
    context["object_list"] = Product.objects.filter(
        category__id=pk,
        availability=True,
        delete=False
    )
    context["category_pk"] = pk
    return render(request, "product/products.html", context)
