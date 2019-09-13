from django import forms

from .models import Ingredient


class IngredientForm(forms.ModelForm):
  
    class Meta:
        model = Ingredient
        fields = ('name', 'article_number','cost_per_unit', 'unit_name' ,'unit_amount','picture','category')
