from django.shortcuts import render,\
    HttpResponse, redirect
from product.views import products


def test(request):
    return HttpResponse('test')


def home(request):
    return redirect('products')
