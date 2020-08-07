from django.contrib import admin
from product.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    readonly_fields = [
        "price",
        "user",
        "quantity_purchases",
        "availability"
    ]
    # цикл для отображения всех полей [field.name for field in Product._meta.get_fields()]
    list_display = ["title", "id", "user", "category", "price"]
    search_fields = ["title", "description", "user__username"]
    list_filter = ["category"]
    list_editable = ["price"]



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    # list_editable = ["title"]
    list_display = [field.name for field in Category._meta.get_fields()[2:]]
    # list_filter = ["title"]

