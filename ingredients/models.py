from django.db import models

class Ingredient(models.Model):
    #
    name = models.CharField(max_length=255,unique=True)
    article_number = models.IntegerField(unique=True)
    cost_per_unit = models.FloatField(default=1)
    unit_name = models.CharField(
        max_length=255,
        choices=(
            ("g","g"),
            ("kg", "kg"),
            ("cl", "cl"),
            ("l","l"),
        ),
        default="kg"
    )
    unit_amount = models.FloatField(default=1)
    #
    picture = models.ImageField(upload_to='ingredients/', blank=True,null=True)
    category = models.CharField(
        max_length=255,
        choices=(
            ("Vegetables", "Vegetables"),
            ("Fruits", "Fruits"),
            ("Fish","Fish"),
            ("Grains", "Grains"),
            ("Added Sweeteners","Added Sweeteners"),
            ("Spices", "Spices"),
            ("Meats", "Meats"),
            ("Seafood", "Seafood"),
            ("Condiments", "Condiments"),
            ("Oils", "Oils"),
            ("Seasoning", "Seasoning"),
            ("Sauces", "Sauces"),
            ("Legumes", "Legumes"),
            ("Alcohol", "Alcohol"),
            ("Soup", "Soup"),
            ("Nuts", "Nuts"),
            ("Dessert & Snack", "Dessert & Snack"),
            ("Beverages", "Beverages"),

        ),
        default="Fruits"
    )
