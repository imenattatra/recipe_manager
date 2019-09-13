from django.contrib import admin
from ingredients.models import Ingredient
# Register your models here.


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
