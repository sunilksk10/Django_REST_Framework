from django.urls import path, include
from api import views

urlpatterns = [
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/
  # Method      : POST 
  # Description : create a recipe
  # {
  #   "user": 1,
  #   "name": "Recipe 1",
  #   "step": [{"step_text": "step 1"}, {"step_text" : "step 2"}],
  #   "ingredient": [{"ingredient_text":"ingredient 1"}, {"ingredient_text":"ingredient 2"}]
  # }
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/
  # Method      : GET 
  # Description : retrieve all recipes
  # <------------------------------------------------->
  path('recipes/', views.ListCreateRecipe.as_view(), name='recipe_list_create'),


  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1 <-- Recipe ID
  # Method      : GET 
  # Description : get Recipe 1(recipe ID)
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1 <-- Recipe ID
  # Method      : PUT
  # Description : Edit Recipe 1(recipe ID)
  # {
  #   "user": 1,
  #   "name": "Recipe 1",
  #   "step": [{"step_text": "step 1"}, {"step_text" : "step 2"}],
  #   "ingredient": [{"ingredient_text":"ingredient 1"}, {"ingredient_text":"ingredient 2"}]
  # }
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1
  # Method      : DELETE 
  # Description : delete Recipe 1(recipe ID)
  # <------------------------------------------------->
  path('recipes/<int:pk>/', views.RetrieveUpdateDestroyRecipe.as_view(), name='recipe_RUD'),

  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/user/1 <-- User ID
  # Method      : GET
  # Description : retrieve list of Recipes belong to a user via User ID
  # <------------------------------------------------->
  path('recipes/user/<int:pk>/', views.UserRecipeList.as_view(), name='user_list'),

  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/user/1/recipe/1
  # Method      : GET
  # Description : Give me the Recipe 1(recipe ID) that's belongs to User 1(user ID)
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/user/1/recipe/1
  # Method      : PUT
  # Description : Update Recipe 1(recipe ID) that belongs to User 1(user ID)
  # {
  #   "user": 1,
  #   "name": "Recipe 1",
  #   "step": [{"step_text": "step 1"}, {"step_text" : "step 2"}],
  #   "ingredient": [{"ingredient_text":"ingredient 1"}, {"ingredient_text":"ingredient 2"}]
  # }
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/user/1/recipe/1
  # Method      : DELETE 
  # Description : delete Recipe 1(recipe ID) belongs to User 1(user ID)
  # <------------------------------------------------->
  path('recipes/user/<int:pk>/recipe/<int:recipe_id>/', views.UserRecipeRetrieveUpdateDestroy.as_view()),

  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1/step/
  # Method      : POST 
  # { "step_text": "step 1" }
  # Description : create a steps for Recipe 1(recipe ID)
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1/step/
  # Method      : GET
  # Description : retrieve all steps related to Recipe 1(recipe ID)
  # <------------------------------------------------->
  path('recipes/<int:pk>/step/', views.ListCreateStep.as_view(), name='step_list_create'),

  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/step/1/
  # Method      : GET
  # Description : Get Step 1(step ID) that related to Recipe 1(recipe ID)
  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/step/1/
  # Method      : PUT/PATCH
  # Description : Update Step 1(step ID) related to Recipe 1(recipe ID)
  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/step/1/
  # Method      : DELETE
  # Description : DELETE Step 1(step ID) related to Recipe 1(recipe ID)
  # <------------------------------------------------->
  path('recipes/<int:recipe_id>/step/<int:pk>/', views.RetrieveUpdateDestroyStep.as_view(), name='step_detail'),

  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1/ingredient/
  # Method      : GET
  # Description : retrieve all ingredients related to Recipe 1(recipe ID)
  # <------------------------------------------------->
  # Endpoint    : http://127.0.0.1:8000/api/recipes/1/ingredient/
  # { "ingredient_text" : "ingredient 1" }
  # Method      : POST 
  # Description : create an ingredient for Recipe 1(recipe ID)
  # <------------------------------------------------->
  path('recipes/<int:pk>/ingredient/', views.ListCreateIngredient.as_view(), name='ingredient_list'),

  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/ingredient/1/
  # Method      : GET
  # Description : Get Ingredient 1(ingredient ID) that related to Recipe 1(recipe ID)
  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/ingredient/1/
  # Method      : PUT/PATCH
  # { "id": 1, "recipe": 1, "ingredient_text": "ingredient 1" }
  # Description : Update Ingredient 1(ingredient ID) related to Recipe 1(recipe ID)
  # <------------------------------------------------->
  # Endpoint    : 127.0.0.1:8000/api/recipes/1/ingredient/1/
  # Method      : DELETE
  # Description : DELETE Ingredient 1(ingredient ID) related to Recipe 1(recipe ID)
  # <------------------------------------------------->
  path('recipes/<int:recipe_id>/ingredient/<int:pk>/', views.RetrieveUpdateDestroyIngredient.as_view(), name='ingredient_detail'),
]