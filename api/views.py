from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, ContactSerializer, Recipe,RecipeSerializer, Step, StepSerializer, Ingredient, IngredientSerializer

class ContactsView(APIView):
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, contact_id):
        
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        


class RecipesView(APIView):
    def get(self, request, recipe_id=None):

        if recipe_id is not None:
            recipe = Recipe.objects.get(id=recipe_id)
            serializer = RecipeSerializer(recipe, many=False)
            return Response(serializer.data)
        else:
            recipes = Recipe.objects.all()
            serializer = RecipeSerializer(recipes, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, recipe_id):
        
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
   
        
class StepsView(APIView):
    def get(self, request, step_id=None):

        if step_id is not None:
           step = Step.objects.get(id=step_id)
           serializer = StepSerializer(step, many=False)
           return Response(serializer.data)
        else:
            steps = Step.objects.all()
            serializer = StepSerializer(steps, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = StepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, recipe_id):
        
        step = Step.objects.get(id=step_id)
        step.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
                
        
        
        
class IngredientsView(APIView):
    def get(self, request, ingredient_id=None):

        if ingredient_id is not None:
            ingredient = Ingredient.objects.get(id=ingredient_id)
            serializer = IngredientSerializer(ingredient, many=False)
            return Response(serializer.data)
        else:
            ingredients = Ingredient.objects.all()
            serializer = IngredientSerializer(ingredients, many=True)
            return Response(serializer.data)
        
    def post(self, request):
            
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self, request, ingredient_id):
        
        ingredient = Ingredient.objects.get(id=ingredient_id)
        ingredient.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
                