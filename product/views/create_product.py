from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, View
from django.utils.decorators import method_decorator
from product.models import Product, Category
from product.forms import ProductForm


@login_required(login_url="/personaloffice/")
class ProductCreate(View):
    def get(self, *args, **kwargs):
        context = {}
        context["form"] = ProductForm()

        return render(
            self.request,
            "product/create.html",
            context    
        )

    def post(self, *args, **kwargs):
        context = {}

        form = ProductForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            new_product = form.save()
            new_product.user = self.request.user
            new_product.save()
            context["products"] = Product.objects.filter(
                availability=True,
                delete=False
            )
            context["message"] = "Товар добавлен"
            return render(self.request, "product/products.html", context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = Product
    fields = [
                "title",
                "category",
                "image",
                "description",
                "price",
            ]

    # form = ProductForm
    template_name = "product/create.html"
    success_url = reverse_lazy("products")
