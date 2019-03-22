from rest_framework import serializers
from django.db import models

# Create your models here. 
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()
        
        
        
#Step model

class Step(models.Model):
    step_text = models.CharField(max_length=50)
   

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        exclude = ()



#Ingredient model

class Ingredient(models.Model):
    text = models.CharField(max_length=50)
    
    

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ()



#Recipe model 

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    
    

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ()