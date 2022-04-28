from django.urls import path

from recipes.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    log_rating,
    RecipeDetailView,
    RecipeListView,
    UserListView,
    create_shopping_item,
    delete_all_shopping_items,
    ShoppingItemListView,
)

from tags.views import (
    TagListView,
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    path("tags/list/", TagListView.as_view(), name="tags_list"),
    path("users/", UserListView.as_view(), name="users_list"),
    path("shopping_items/", ShoppingItemListView.as_view(), name="shopping_item_list"),
    path("shopping_items/create/", create_shopping_item, name="shopping_item_create"),
    path("shopping_items/delete/", delete_all_shopping_items, name="delete_all_shopping_items"),
]
