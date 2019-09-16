from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ingredients.views import *
from recipes.views import *
from apicbase import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #list and crud URLS for ingredients
    path('ingredients/', IngredientList.as_view(), name='all_ingredients'),
    path('ingredients/add/', IngredientCreate.as_view(), name='add_ingredient'),
    path('ingredients/<int:pk>/delete/', IngredientDelete.as_view(), name='delete_ingredient'),
    path('ingredients/<int:pk>/edit/', IngredientEdit.as_view(), name='edit_ingredient'),
    
    #list and crud URLS for recipes
    path('', RecipeList.as_view(), name='all_recipes'),
    path('recipes/', RecipeList.as_view(), name='all_recipes'),
    path('recipes/add/', RecipeCreate.as_view(), name='add_recipe'),
    path('recipes/<int:pk>/delete/', RecipeDelete.as_view(), name='delete_recipe'),
    path('recipes/<int:pk>/edit/', RecipeEdit.as_view(), name='edit_recipe'),
    path('recipes/<int:pk>/detail/', RecipeDetail.as_view(), name='view_recipe'),

    #list and crud for recipe ingredients(ingredient+amount for the recipe)
    path('recipes/<int:recipe_id>/recipeingredient/add/',create_recipe_ingredient,name='add_recipe_ingredient'),
    path('recipes/<int:recipe_id>/recipeingredient/<int:pk>/delete/',RecipeIngredientDelete.as_view(),name='delete_recipe_ingredient'),
    path('recipes/<int:recipe_id>/recipeingredient/<int:pk>/edit/',edit_recipe_ingredient,name='edit_recipe_ingredient'),

    #Ajax calls to check existence of ingredient/recipe while creating
    path('check_ingredient_by_number', check_ingredient_by_number, name='check_ingredient_by_number'),
    path('check_ingredient_by_name', check_ingredient_by_name, name='check_ingredient_by_name'),
    path('check_recipe_by_name', check_recipe_by_name, name='check_recipe_by_name'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)