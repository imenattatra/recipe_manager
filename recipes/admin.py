from django.contrib import admin

from recipes.models import Recipe,RecipeIngredient
# Register your models here.
@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
