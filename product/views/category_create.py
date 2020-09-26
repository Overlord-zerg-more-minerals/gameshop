from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, View
from django.utils.decorators import method_decorator
from product.models import Category


class CategoryCreate(CreateView):
    model = Category
    fields = ["name", "description"]
    tamplate_name = "product/create_category.html"
    success_url = reverse_lazy("products")

    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda user: user.is_staff)
# def create_category(request):
#     context = {}

#     if request.method == "POST":
#         form = CategoryCreateForm(request.POST)
#         if form.is_valid():
#             category = form.save()
#             return redirect("category", pk=category.id)

#     context["form"] = CategoryCreateForm()
#     return render(request, "product/create_category.html", context)
