from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView,ListView,CreateView
from recipes.models import Recipe,RecipeIngredient
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from recipes.forms import RecipeForm,RecipeIngredientForm
"""
Recipe INGREDIENT CRUD views ( iNGREDIENT + amount of this ingredient for the recipe)
"""
class RecipeIngredientCreate(CreateView):
    model = RecipeIngredient
    template_name = "Recipes/add_recipe_ingredient.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(RecipeIngredientCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add Recipe Ingredient'
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong.")
        return self.render_to_response(
        self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        form.save()
        print(form)
        #FIXME correct redirection
        messages.success(self.request, "Ingredient addedd successfully to the recipe.")
        #we redirect to the "edit recipe" 
        return HttpResponseRedirect('/recipes/')
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