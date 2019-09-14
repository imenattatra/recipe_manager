from django.db import models
from django.db.models import Sum
from ingredients.models import Ingredient

APPETIZERS="Appetizers"
BEVERAGE="Beverage"
SOUPS="Soups"
SALADS="Salads"
MAIN_DISHES="Main dishes"
BREADS="Breads"
ROLLS="Rolls"
DESSERT="Dessert"
MISSELANEOUS="Misselaneous"
        
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='recipes/', blank=True,null=True)
    category=models.CharField(
        max_length=100,
        choices=(
            (APPETIZERS, APPETIZERS),
            (BEVERAGE, BEVERAGE),
            (SOUPS, SOUPS),
            (SALADS, SALADS),
            (MAIN_DISHES, MAIN_DISHES),
            (BREADS, BREADS),
            (ROLLS, ROLLS),
            (DESSERT, DESSERT),
            (MISSELANEOUS, MISSELANEOUS),
        ),
        default=MAIN_DISHES
    )
    @property
    def get_total_cost(self):
        list_recipe_ingredients=self.recipeingredient_set.all()
        som=0
        for elem in list_recipe_ingredients:
            som=som+elem.get_cost
        return som

class RecipeIngredient(models.Model):
    ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount=models.FloatField()
    recipe= models.ForeignKey(Recipe, on_delete=models.CASCADE)

    @property
    def get_cost(self):
        cost=(self.amount*self.ingredient.cost_per_unit)/self.ingredient.unit_amount
        return cost


