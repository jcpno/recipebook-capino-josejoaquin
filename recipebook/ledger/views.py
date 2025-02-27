from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'
    recipes = Recipe.objects.all()

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'