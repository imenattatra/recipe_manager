# Generated by Django 2.2.5 on 2019-09-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_auto_20190914_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Fish', 'Fish'), ('Grains', 'Grains'), ('Added Sweeteners', 'Added Sweeteners'), ('Spices', 'Spices'), ('Meats', 'Meats'), ('Seafood', 'Seafood'), ('Condiments', 'Condiments'), ('Oils', 'Oils'), ('Seasoning', 'Seasoning'), ('Sauces', 'Sauces'), ('Legumes', 'Legumes'), ('Alcohol', 'Alcohol'), ('Soup', 'Soup'), ('Nuts', 'Nuts'), ('Dessert & Snack', 'Dessert & Snack'), ('Beverages', 'Beverages')], default='Fruits', max_length=255),
        ),
    ]
