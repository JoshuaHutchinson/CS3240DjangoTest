from django import forms
from .models import DeepThought


class DeepThoughtForm(forms.ModelForm):
    class Meta:
        model = DeepThought
        fields = ["deepThought_title", "deepThought_text"]
