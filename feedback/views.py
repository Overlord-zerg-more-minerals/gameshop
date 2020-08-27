# from django.shortcuts import render
# from django.views.decorators.http import require_POST


# @require_POST
# def feedback(request):
#     context = {}

#     form = FeedBackForm(request.POST, request.FILES)
#     if form.is_valid():
#         feedback = form.save()
#         if request.user.is_authenticated:
#             feedback.user = request.user
#             feedback.save()

#         context["massege"] = "Ваше обращение принято, Пока"
#         context["type"] = "info"
#         return render(request, "core/massege.html", context)
    
#     context["massege"] = "Упс, Ошибочка"
#     context["type"] = "danger"
#     return render(request, "core/massege.html", context)