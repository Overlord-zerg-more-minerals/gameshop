from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, DetailView
from product.models import Product


def product(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    return render(request, "product/product.html", context)


class ProductView(TemplateView):
    template_name = "product/product.html"

    def get_context_data(self, **kwargs): # pk = 3
        context = {}
        pk = self.kwargs["pk"]
        product = Product.objects.get(id=pk)
        context["product"] = product
        return context


class ProductDetailView(DetailView):
    template_name = "product/product.html"
    model = Product


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
