from django.db import models


# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length = 125)
  author = models.CharField(max_length = 100)
  description = models.TextField()
  image = models.URLField(null = True, blank = True)
  created = models.DateTimeField(auto_now_add = True)
  updated = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.name + " by " + self.author
    

class Measure(models.Model):
  name = models.CharField(max_length = 30, unique = True)
  abbreviation = models.CharField(max_length = 10, unique = True)

  def __str__(self):
    return self.name + " (" + self.abbreviation + ")"

class FoodItem(models.Model):
  name = models.CharField(max_length = 100, unique = True)

  def __str__(self):
    return self.name

class Ingredient(models.Model):
  amount = models.FloatField()
  recipe = models.ForeignKey(
    Recipe,
    related_name = "Recipe",
    on_delete = models.CASCADE,
  )
  measure = models.ForeignKey(
    Measure,
    related_name = "Measure",
    on_delete = models.PROTECT,
  )
  food = models.ForeignKey(
    FoodItem,
    related_name = "FoodItem",
    on_delete = models.PROTECT,
  )

  def __str__(self):
    return self.amount + " " + self.measure + " of " + self.food
