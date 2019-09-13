from django import forms
from recipes.models import Recipe,RecipeIngredient

class RecipeForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(queryset=Tache.objects.all(), required=False)
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'
        