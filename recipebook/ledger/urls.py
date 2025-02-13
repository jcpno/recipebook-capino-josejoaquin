from django.urls import path

from . import views

urlpatterns = [
    path("recipes/list", views.recipes_list, name="recipes-list"),
    #path("/recipe/1", views.index),
    #path("/recipe/2", views.index)
]

app_name = "ledger"