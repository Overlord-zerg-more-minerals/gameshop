from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from core.forms import PasswordChangeForm


@require_http_methods(["POST"])
def change_password(request):
    context = {}
    if request.method == "POST":
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personaloffice", pk=user.id)

    context["form"] = PasswordChangeForm(User)
    # core/edit_personaloffice.html
    return render(request, "core/personaloffice.html")
