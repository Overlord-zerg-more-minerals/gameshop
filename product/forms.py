from django import forms
from product.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "category",
            "image",
            "description",
            "price",
        ]

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "title",
            "description"
        ]