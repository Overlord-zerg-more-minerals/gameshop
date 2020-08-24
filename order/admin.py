from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = OrderAdmin
    list_display = ["title", "phone", "get_product_count"]
    inlines = [
        ProductInOrderInline
    ]

    def get_product_count(self, obj):
        return obj.product_in_order.count()
    

@admin.register(ProductInOrderInline)
class ProductInOrderAdmin(admin.ModelAdmin):
    model = ProductInOrder
    list_display = ("order", "product", "added")
    list_fields = ["order", "product", "added"]
