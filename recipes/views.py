from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView,ListView,CreateView
from recipes.models import Recipe
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

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
    template_name = "Ingredients/add_ingredient.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(IngredientCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add Ingredient'
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong")
        return self.render_to_response(
        self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ingredient added successfully")
        return HttpResponseRedirect('/ingredients/')

class RecipeDelete(DeleteView):
    model = Recipe
    def get_success_url(self):
        messages.success(self.request, "Recipe deleted successfully")
        return reverse('all_recipes')

class RecipeEdit(UpdateView):
    pass