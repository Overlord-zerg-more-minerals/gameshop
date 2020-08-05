from django.shortcuts import render,\
    HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.forms import RegistrationForm
from product.models import Product


def test(request):
    return HttpResponse('test')


def home(request):
    return redirect('products')


def personaloffice(request, pk):
        context = {}
        context["user"] = User.objects.get(id=pk)
        context["products"] = Product.objects.filter(user=context["user"])
        return render(request, "core/personaloffice.html", context)


def login(request):
    if request.user.is_authenticated:
        return redirect(personaloffice)
    context = {}
    if "login" in request.POST:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(personaloffice)

    context["form"] = AuthenticationForm()
    return render(request, "core/login.html", context)


def logout(request):
    auth.logout(request)
    return redirect(personaloffice)


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(personaloffice)

    context = {}
    context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)


def sellers(request):
    sellers = User.objects.exclude(product=None)
    context = {"sellers": sellers}
    return render(request, "core/sellers.html", context)
