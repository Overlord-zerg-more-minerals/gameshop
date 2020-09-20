from django.urls import path 
from product.views import *


urlpatterns = [
    path('all', ProductList.as_view(), name="products"),
    path('category/<int:pk>/', category, name="category"),
    path('category/create/', CategoryCreate.as_view(), name="category-create"),
    path('<int:pk>/', ProductDetailView.as_view(), name="product"),
    path('create/', ProductCreateView.as_view(), name="create-product"),
    path('create-few/', create_few, name="create-few"),
    path('edit/<int:id>/', edit_product, name="edit-product"),
    path('delete/<int:id>/', delete_product, name="delete-product")
]