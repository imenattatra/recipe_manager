from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView,ListView,CreateView
from recipes.models import Recipe,RecipeIngredient
from ingredients.models import Ingredient
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from recipes.forms import RecipeForm,RecipeIngredientForm


"""
Recipe CRUD views
"""
class RecipeList(ListView):
    model = Recipe
    template_name = "Recipes/all_recipes.html"
    context_object_name = "all_recipes"
    def get_context_data(self, **kwargs):
        context = super(RecipeList, self).get_context_data(**kwargs)
        context['title'] = 'Recipes List'
        return context

class RecipeCreate(CreateView):
    model = Recipe
    template_name = "Recipes/add_recipe.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(RecipeCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add Recipe'
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong")
        return self.render_to_response(
        self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        c=form.save()
        messages.success(self.request, "Recipe created successfully, you can now add ingredients to your recipe")
        #we redirect to the "edit recipe" so the user can add ingrediants
        id=c.id
        return HttpResponseRedirect('/recipes/'+str(id)+'/edit/')

class RecipeDelete(DeleteView):
    model = Recipe
    def get_success_url(self):
        messages.success(self.request, "Recipe deleted successfully")
        return reverse('all_recipes')

class RecipeEdit(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'Recipes/edit_recipe.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super(RecipeEdit, self).get_context_data(**kwargs)
        context['title'] = 'Edit Recipe'
        context['all_ingredients'] = Ingredient.objects.all()
        context['all_recipe_ingredients'] = RecipeIngredient.objects.filter(recipe_id=self.kwargs.get('pk'))
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong")
        return self.render_to_response(
        self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Recipe modified successfully")
        return HttpResponseRedirect('/recipes/')

"""
Recipe INGREDIENT CRUD views (Recipe INGREDIENT=iNGREDIENT + amount of this ingredient for the recipe)
"""
def create_recipe_ingredient(request,recipe_id):
    #FIXME : apply createView with modal to keep the same coding logic
    if request.method == "POST":

        ingredient =Ingredient.objects.get(id=request.POST.get("ingredient"))
        recipe=Recipe.objects.get(id=recipe_id)
        amount = request.POST.get("amount")
        try :
            RecipeIngredient(recipe=recipe,ingredient=ingredient,amount=amount).save()
            messages.success(request, "Ingredient addedd successfully to the recipe.")
        except:
            messages.error(request, "Something went wrong.")
    return HttpResponseRedirect('/recipes/' + str(recipe_id) + '/edit/')

def edit_recipe_ingredient(request,recipe_id,pk):
    #FIXME : apply editView with modal to keep the same coding logic
    if request.method == "POST":

        ingredient =Ingredient.objects.get(id=request.POST.get("ingredient"))
        amount = request.POST.get("amount")
        try :
            ing=RecipeIngredient.objects.filter(id=pk).update(ingredient=ingredient,amount =amount )

            messages.success(request, "Recipe's ingredient updated successfully.")
        except :
            messages.error(request, "Something went wrong.")
    return HttpResponseRedirect('/recipes/' + str(recipe_id) + '/edit/')

class RecipeIngredientDelete(DeleteView):
    model = RecipeIngredient
    def get_success_url(self):
        messages.success(self.request, "Ingredient deleted successfully from the recipe")
        return reverse('edit_recipe', kwargs={'pk': self.kwargs.get('recipe_id')})
