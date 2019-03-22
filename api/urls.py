from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    
    
    path('steps/<int:step_id>', views.StepsView.as_view(), name='id-steps'),
    path('steps/', views.StepsView.as_view(), name='all-steps'),
    
    
    path('ingredients/<int:ingredient_id>', views.IngredientsView.as_view(), name='id-ingredients'),
    path('ingredients/', views.IngredientsView.as_view(), name='all-ingredients'),
    
    
    path('recipes/<int:recipe_id>', views.RecipesView.as_view(), name='id-recipes'),
    path('recipes/', views.RecipesView.as_view(), name='all-recipes'),
    
]


