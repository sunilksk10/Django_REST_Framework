from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=250, null=False)

class Step(models.Model):
  step_text = models.CharField(max_length=250, null=False)
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='step')

class Ingredient(models.Model):
  ingredient_text = models.CharField(max_length=250, null=False)
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredient')

  def __str__(self):
    return self.ingredient_text