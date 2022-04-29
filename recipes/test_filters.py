from unittest import TestCase
from recipes.models import Ingredient, Recipe
from recipes.templatetags.resizer import resize_to

class ResizeToTests(TestCase):
  def test_error_when_ingredient_is_none(self):
    #arrange
    #act
    with self.assertRaises(AttributeError):
      resize_to(None,3)
    #assert

  def test_recipe_has_no_serving(self):
    #arrange
    recipe = Recipe(servings=None)
    ingredient = Ingredient(recipe=recipe, amount = 5)
    #act
    result = int(resize_to(ingredient,None))
    #assert
    self.assertEqual(5, float(result))
  
  def test_resize_to_is_none(self):
    recipe = Recipe(servings = 2)
    ingredient = Ingredient(recipe=recipe,amount = 5)

    result = resize_to(ingredient,None)

    self.assertEqual(5, float(result))
  
  def test_values_for_servings_amount_and_target(self):
    recipe = Recipe(servings = 2)
    ingredient = Ingredient(recipe=recipe,amount = 5)

    result = resize_to(ingredient,10)

    self.assertEqual(25, float(result))

  def test_target_is_letters(self):
    recipe = Recipe(servings = 2)
    ingredient = Ingredient(recipe=recipe,amount = 5)

    result = resize_to(ingredient,"abc")

    self.assertEqual(5, float(result))
