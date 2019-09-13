from django.contrib import admin

from recipes.models import Recipe
# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
