from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def change_password(request):
    context = {}
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personaloffice", pk=user.id)

    context["password_change_form"] = ChangePasswordForm()
    # core/edit_personaloffice.html
    return render(request, "core/personaloffice.html")
