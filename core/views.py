from django.shortcuts import render,\
    HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from core.forms import RegistrationForm


def test(request):
    return HttpResponse('test')


def home(request):
    return redirect('products')


def personaloffice(request):
    return render(request, "core/personaloffice.html")


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
