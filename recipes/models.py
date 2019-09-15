from django.db import models
from django.db.models import Sum
from ingredients.models import Ingredient
        
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='recipes/', blank=True,null=True)
    category=models.CharField(
        max_length=255,
        choices=(
            ("Appetizers", "Appetizers"),
            ("Beverage", "Beverage"),
            ("Soups", "Soups"),
            ("Salads", "Salads"),
            ("Main dishes", "Main dishes"),
            ("Breads", "Breads"),
            ("Rolls", "Rolls"),
            ("Dessert", "Dessert"),
            ("Misselaneous", "Misselaneous"),
        ),
        default= "Main dishes"
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


