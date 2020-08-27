from django import forms
from .models import Feedback


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "text", "screen", "phone", "email"]