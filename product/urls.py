from django.urls import path 
from product.views import *


urlpatterns = [
    path('all', products, name="products"),
    path('category/<int:pk>/', category, name="category"),
    path('<int:id>/', product, name="product"),
    path('cbv/', ProductView.as_view()),
    path('create/', create_product, name="create-product"),
    path('create-few/', create_few, name="create-few"),
    path('edit/<int:id>/', edit_product, name="edit-product"),
    path('delete/<int:id>/', delete_product, name="delete-product")
]