from rest_framework import serializers
from django.db import models


#User model

class User(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ()



#Step model

class Step(models.Model):
    step_text = models.CharField(max_length=500)
    #recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, default="dinner")
   

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        exclude = ()


#Recipe model 

class Recipe(models.Model):
    name = models.CharField(max_length=500)
    #user = models.ForeignKey("User", on_delete=models.SET_NULL, blank=True, null=True,)
    #step= models.ForeignKey("Step", on_delete=models.CASCADE)
    #ingredient= models.ForeignKey("Ingredient", on_delete=models.CASCADE)

    

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ()        






#Ingredient model

class Ingredient(models.Model):
    text = models.CharField(max_length=500)
    
    

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ()



