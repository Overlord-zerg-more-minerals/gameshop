from django.contrib import admin
from product.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    readonly_fields = [
        "price",
        "user",
        "delete",
        "quantity_purchases",
        "quantity_purchases",
        "availability"
    ]
    list_display = [field.name for field in Product._meta.get_fields()]
    list_display_links = ("id", "title", "user")
    list_editable = ("price",)
    search_fields = ["title", "description", "user__username"]
    list_filter = ["category", "title"]
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = [field.name for field in Category._meta.get_fields() if field.name not in ["product", "child_category"]]
    list_editable = [f.name for f in Category._meta.get_fields() if f.name not in ["id", "product", "child_category"]]
    search_fields = ["title", "product__title"]
