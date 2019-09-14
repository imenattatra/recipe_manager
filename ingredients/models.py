from django.db import models

# Unit name choices
GRAMS = "g"
KILOGRAMS = "kg"
CENTILITER = "cl"
LITER = "l"
# Category choices
DIARY = "Diary"
VEGETABLES = "Vegetables"
FRUITS = "Fruits"
FISH = "Fish"
BAKING_GRAINS = "Backing & GRains"
ADDED_SWEETENERS = "Added Sweeteners"
SPICES = "Spices"
MEATS = "Meats"
SEAFOOD = "Seafood"
CONDIMENTS = "Condiments"
OILS = "Oils"
SEASONING = "Seasoning"
SAUCES = "Sauces"
LEGUMES = "Legumes"
ALCOHOL = "Alcohol"
SOUP = "Soup"
NUTS = "Nuts"
DESSERT_SNACK = "Dessert & Snack"
BEVERAGES = "Beverages"


class Ingredient(models.Model):
    #
    name = models.CharField(max_length=255,unique=True)
    article_number = models.IntegerField(unique=True)
    cost_per_unit = models.FloatField(default=1)
    unit_name = models.CharField(
        max_length=255,
        choices=(
            (GRAMS, GRAMS),
            (KILOGRAMS, KILOGRAMS),
            (CENTILITER, CENTILITER),
            (LITER, LITER),
        ),
        default=KILOGRAMS
    )
    unit_amount = models.FloatField(default=1)
    #
    picture = models.ImageField(upload_to='ingredients/', blank=True,null=True)
    category = models.CharField(
        max_length=255,
        choices=(
            (DIARY, DIARY),
            (VEGETABLES, VEGETABLES),
            (FRUITS, FRUITS),
            (BAKING_GRAINS, BAKING_GRAINS),
            (ADDED_SWEETENERS, ADDED_SWEETENERS),
            (SPICES, SPICES),
            (MEATS, MEATS),
            (SEAFOOD, SEAFOOD),
            (CONDIMENTS, CONDIMENTS),
            (OILS, OILS),
            (SEASONING, SEASONING),
            (SAUCES, SAUCES),
            (LEGUMES, LEGUMES),
            (ALCOHOL, ALCOHOL),
            (SOUP, SOUP),
            (NUTS, NUTS),
            (DESSERT_SNACK, DESSERT_SNACK),
            (BEVERAGES, BEVERAGES),

        ),
        default=FRUITS
    )
