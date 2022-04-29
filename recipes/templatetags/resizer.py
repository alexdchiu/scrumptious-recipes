from django import template

register = template.Library()


def resize_to(ingredient, target):
  servings = ingredient.recipe.servings
  amount = ingredient.amount
  if servings is not None and target is not None:
    print(amount)
    try:
      ratio = int(target) / int(servings)
      amount = ratio * amount
    except:
      pass
  return str(amount)



register.filter(resize_to)