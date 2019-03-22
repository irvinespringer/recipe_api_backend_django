from django.contrib import admin
from api.models import Contact, Step, Ingredient, Recipe
#Model registration below
admin.site.register(Contact)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Recipe)