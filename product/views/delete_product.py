from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product


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