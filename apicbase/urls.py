"""apicbase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('recipes/', RecipeList.as_view(), name='all_recipes'),
    path('recipes/add/', RecipeCreate.as_view(), name='add_recipe'),
    path('recipes/<int:pk>/delete/', RecipeDelete.as_view(), name='delete_recipe'),
    path('recipe/<int:pk>/edit/', RecipeEdit.as_view(), name='edit_recipe'),
    #path('recipe/<int:pk>/detail/', IngredientDetail.as_view(), name='details_recipe'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)