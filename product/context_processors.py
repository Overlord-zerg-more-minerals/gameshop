from product.models import Category
# from feedback.models import FeedBackForm


def category(request):
    context = {}
    context["categories"] = Category.objects.order_by("title")
    # context["Feedback_form"] = FeedBackForm()
    return context
