# Generated by Django 2.2.5 on 2019-09-13 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='ingredients/')),
                ('category', models.CharField(choices=[('Appetizers', 'Appetizers'), ('Beverage', 'Beverage'), ('Soups', 'Soups'), ('Salads', 'Salads'), ('Main dishes', 'Main dishes'), ('Breads', 'Breads'), ('Rolls', 'Rolls'), ('Dessert', 'Dessert'), ('MIsselaneous', 'MIsselaneous')], default='Main dishes', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe')),
            ],
        ),
    ]
