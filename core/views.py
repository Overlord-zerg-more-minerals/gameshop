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
        return redirect(home)
    context = {}
    if "login" in request.POST:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect(home)

    context["form"] = AuthenticationForm()
    return render(request, "core/login.html", context)


def logout(request):
    auth.logout(request)
    return redirect(home)


def registration(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2 and form.is_valid():
            form.save()
            return redirect("login")
        else:
            context["form"] = form
            context["massege"] = "Форма заполнена неверно и/или пароли не совпадают"
    else:   
        context["form"] = RegistrationForm()
    return render(request, "core/registration.html", context)


def sellers(request):
    sellers = User.objects.exclude(product=None)
    context = {"sellers": sellers}
    return render(request, "core/sellers.html", context)
