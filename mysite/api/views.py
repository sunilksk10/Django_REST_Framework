from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)

from api.serializers import RecipeSerializer, StepSerializer, IngredientSerializer
from api.models import Recipe, Step, Ingredient

"""
User Recipe Views
"""
class UserRecipeList(generics.ListAPIView):
  """ 
  Get list of recipes that belongs to a user via User ID
  """
  serializer_class = RecipeSerializer

  def get_queryset(self):
    queryset = Recipe.objects.all()
    user = get_object_or_404(User, id=self.kwargs.get('pk'))
    
    if user:
      return queryset.filter(user__id=user.id)

class UserRecipeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  """ 
  * Get individual Recipe that belongs to a user via Recipe ID
  * Update/Delete a Recipe via Recipe ID
  """
  serializer_class = RecipeSerializer
  queryset = Recipe.objects.all()

  def get_object(self):
    recipe_id = self.kwargs.get('recipe_id')
    user = get_object_or_404(User, id=self.kwargs.get('pk'))
    recipe = get_object_or_404(Recipe, id=recipe_id, user=user)
    return recipe

"""
Recipe Views
"""

class ListCreateRecipe(generics.ListCreateAPIView):
  """ 
  * Get all the Recipes 
  * Create a Recipe 
  """
  serializer_class = RecipeSerializer
  queryset = Recipe.objects.all()

  def create(self, request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
      recipe = serializer.create(request)
      if recipe:
        return Response(RecipeSerializer(recipe).data, status=HTTP_201_CREATED)
    return Response(status=HTTP_400_BAD_REQUEST)

class RetrieveUpdateDestroyRecipe(generics.RetrieveUpdateDestroyAPIView):
  """ 
  * Get single Recipe via Recipe ID
  * Update/Delete a Recipe via Recipe ID
  """
  serializer_class = RecipeSerializer
  queryset = Recipe.objects.all()

"""
Step Views
"""

class ListCreateStep(generics.ListCreateAPIView):
  """ 
  * Get list of Steps that related to a Recipe 
  * add a Step to a Recipe 
  """
  serializer_class = StepSerializer
  queryset = Step.objects.all()

  def get_queryset(self):
    return self.queryset.filter(recipe_id=self.kwargs.get('pk'))
    
  def perform_create(self, serializer):
    recipe = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
    serializer.save(recipe=recipe)

class RetrieveUpdateDestroyStep(generics.RetrieveUpdateDestroyAPIView):
  """ 
  * Get single Step that related to a recipe via Step ID
  * Update/Delete a Step via Step ID
  """
  serializer_class = StepSerializer
  queryset = Step.objects.all()

  def get_object(self):
    step_id = self.kwargs.get('pk')
    recipe = get_object_or_404(Recipe, id=self.kwargs.get('recipe_id'))
    step = get_object_or_404(Step, id=step_id, recipe=recipe)
    return step

"""
Ingredient Views
"""

class ListCreateIngredient(generics.ListCreateAPIView):
  """ 
  * Get list of Ingredients that related to a Recipe 
  * add an Ingredient to a Recipe
  """
  serializer_class = IngredientSerializer
  queryset = Ingredient.objects.all()

  def get_queryset(self):
    return self.queryset.filter(recipe_id=self.kwargs.get('pk'))
  
  def perform_create(self, serializer):
    recipe = get_object_or_404(Recipe, pk=self.kwargs.get('pk'))
    serializer.save(recipe=recipe)

class RetrieveUpdateDestroyIngredient(generics.RetrieveUpdateDestroyAPIView):
  """ 
  * Get single Ingredient that related to a recipe via ingredient ID
  * Update/Delete an Ingredient via ingredient ID
  """
  serializer_class = IngredientSerializer
  queryset = Ingredient.objects.all()

  def get_object(self):
    ingredient_id = self.kwargs.get('pk')
    recipe = get_object_or_404(Recipe, id=self.kwargs.get('recipe_id'))
    ingredient = get_object_or_404(Ingredient, id=ingredient_id, recipe=recipe)
    return ingredient