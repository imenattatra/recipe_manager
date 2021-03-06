from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView,ListView,CreateView
from .models import Ingredient
from .forms import IngredientForm
from django.urls import reverse
from django.http import JsonResponse

"""
Ingredient CRUD views in this order: 
-IngredientList
-IngredientCreate
-IngredientDelete
-IngredientEdit
"""

class IngredientList(ListView):
    model = Ingredient
    template_name = "all_ingredients.html"
    context_object_name = "all_ingredients"
    def get_context_data(self, **kwargs):
        context = super(IngredientList, self).get_context_data(**kwargs)
        context['title'] = 'Ingredients List'
        return context
    def get_queryset(self):
        queryset = Ingredient.objects.all()
        #filter list of ingredients if we need to
        if self.request.GET.get("key"):
            key = self.request.GET.get("key")
            # if key is number than we filter by article number else we filter by name
            try:
                key=int(key)
            except:
                pass
            if isinstance(key, int):
                queryset=queryset.filter(article_number=key)
            else:
                queryset=queryset.filter(name=key)
        return queryset

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "add_ingredient.html"
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

class IngredientDelete(DeleteView):
    model = Ingredient
    def get_success_url(self):
        messages.success(self.request, "Ingredient deleted successfully")
        return reverse('all_ingredients')
    
class IngredientEdit(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'edit_ingredient.html'
    context_object_name = 'ingredient'

    def get_context_data(self, **kwargs):
        context = super(IngredientEdit, self).get_context_data(**kwargs)
        context['title'] = 'Edit Ingredient'
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong")
        return self.render_to_response(
        self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ingredient modified successfully")
        return HttpResponseRedirect('/ingredients/')


"""
Functions that check existence of ingredient while creating: 
-check_ingredient_by_number
-check_ingredient_by_name
"""

def check_ingredient_by_number(request):
    number = request.GET.get('number', None)  
    data = {
        'is_taken': Ingredient.objects.filter(article_number__iexact=number).exists(),
    }
    return JsonResponse(data)

def check_ingredient_by_name(request):
    name = request.GET.get('name', None)  
    data = {
        'is_taken': Ingredient.objects.filter(name__iexact=name).exists(),
    }
    return JsonResponse(data)