from django.db import models
from ingredients.models import Ingredient

APPETIZERS="Appetizers"
BEVERAGE="Beverage"
SOUPS="Soups"
SALADS="Salads"
MAIN_DISHES="Main dishes"
BREADS="Breads"
ROLLS="Rolls"
DESSERT="Dessert"
MISSELANEOUS="MIsselaneous"
        
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='ingredients/', blank=True,null=True)
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
        #TODO aggreagate by cost

class RecipeIngredient(models.Model):
    ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount=models.FloatField()
    recipe= models.ForeignKey(Recipe, on_delete=models.CASCADE)

    @property
    def get_cost(self):
        cost=(self.amout*self.ingredient.coset_per_unit)/self.ingredient.unit_amount
        return cost


