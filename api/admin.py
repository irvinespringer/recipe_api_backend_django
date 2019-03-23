from django.contrib import admin
from api.models import User, Step, Ingredient, Recipe

#Model registration 

admin.site.register(User)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Recipe)