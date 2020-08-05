from django.contrib import admin
from product.models import *


class ProductAdmin(admin.ModelAdmin):
    model = Category
    # fields = ["title", "user", "category", "price"]
    list_display = ["id", "title", "user", "category", "price"]
    search_fields = ["title", "description", "user__username"]
    list_filter = ["category"]
    

admin.site.register(Product, ProductAdmin)


admin.site.register(Category)
