from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
from product.forms import ProductForm


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
    