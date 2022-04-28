from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError

from recipes.forms import RatingForm
from recipes.models import Recipe, Ingredient, ShoppingItem


USER_MODEL = settings.AUTH_USER_MODEL


def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            try: 
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
            except Recipe.DoesNotExist:
                return redirect("recipes_list")            
    return redirect("recipe_detail", pk=recipe_id)

@require_http_methods(["POST"])
def create_shopping_item(request):
    ingredient_id = request.POST.get("ingredient_id")
    ingredient = Ingredient.objects.get(id=ingredient_id)
    user = request.user

    try:
        ShoppingItem.objects.create(
            food_item = ingredient.food,
            user = user
        )
    
    except IntegrityError:
        pass

    return redirect("recipe_detail", pk = ingredient.recipe.id)

def delete_all_shopping_items(request):
    ShoppingItem.objects.filter(user=request.user).delete()
    return redirect("shopping_items.html")

class RecipeListView(ListView):
    model = Recipe
    paginate_by = 2
    template_name = "recipes/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from pprint import pprint
        pprint(context)
        return context


class UserListView(ListView):
    model = User
    context_object_name = "users"
    template_name = "recipes/users.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from pprint import pprint
        pprint(context)
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.edited_by = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")

class ShoppingItemListView(LoginRequiredMixin, ListView):
    model = ShoppingItem
    template_name = "shopping_items/list.html"

    def get_queryset(self):
        return ShoppingItem.objects.filter(owner=self.request.user)