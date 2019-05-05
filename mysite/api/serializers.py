from rest_framework import serializers
from api.models import Recipe, Step, Ingredient
from django.contrib.auth.models import User

class StepSerializer(serializers.ModelSerializer):
  class Meta:
    model = Step
    fields= ('id', 'step_text',)

    read_only_fields = ['recipe']

class IngredientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredient
    fields= ('id', 'ingredient_text',)

    read_only_fields = ['recipe']

class RecipeSerializer(serializers.ModelSerializer):
  step = StepSerializer(many=True)
  ingredient = IngredientSerializer(many=True)

  class Meta:
    model = Recipe
    fields= ('id', 'user', 'name', 'step', 'ingredient',)

  def create(self, request):
    data = request.data

    recipe = Recipe()
    user = User.objects.get(id=data['user'])

    recipe.user = user
    recipe.name = data['name']
    recipe.save()

    for step in data['step']:
      newStep = Step()
      newStep.recipe = recipe
      newStep.step_text = step['step_text']
      newStep.save()

    for ing in data['ingredient']:
      newIng = Ingredient()
      newIng.recipe = recipe
      newIng.ingredient_text = ing['ingredient_text']
      newIng.save()

    return recipe

  def update(self, instance, validated_data):
    steps_data       = validated_data.pop('step')
    ingredients_data = validated_data.pop('ingredient')

    steps = (instance.step).all()
    steps = list(steps)

    ingredients = (instance.ingredient.all())
    ingredients = list(ingredients)

    instance.name = validated_data.get('name', instance.name)
    instance.user = validated_data.get('user', instance.user)
    instance.save()

    if len(steps) > 0:
      for step_data in steps_data:
        step = steps.pop(0)
        step.step_text = step_data.get('step_text', step.step_text)
        step.save()

    if len(ingredients) > 0:
      for ingredient_data in ingredients_data:
        ingredient = ingredients.pop(0)
        ingredient.ingredient_text = ingredient_data.get('ingredient_text', ingredient.ingredient_text)
        ingredient.save()
  
    return instance
    