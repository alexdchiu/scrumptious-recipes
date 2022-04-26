from django import forms
from recipes.models import Rating


from recipes.models import Recipe


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]