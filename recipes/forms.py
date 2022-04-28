from django import forms
from recipes.models import Rating, ShoppingItem


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]


class ShoppingItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ["user", "food_item"]