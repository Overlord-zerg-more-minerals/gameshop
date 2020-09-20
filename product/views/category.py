from django.shortcuts import render
from django.db.models import Q
from product.models import Product
from product.models.category import Category


def category(request, pk):
    context = {}
    category = Category.objects.get(id=pk)
    context["object_list"] = Product.objects.filter(
        Q(category=category) |
        Q(category__in=category.child_category.all()),
        availability=True,
        delete=False
    )
    context["category_pk"] = pk
    return render(request, "product/products.html", context)
