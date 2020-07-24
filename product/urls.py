from django.urls import path 
from .views import *

urlpatterns = [
    path('all', products, name="products"),
    path('<int:id>/', product, name="product"),
    path('create/', create_product, name="create-product"),
    path('edit/<int:id>/', edit_product, name="edit-product"),
]