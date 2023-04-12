#!/usr/bin/python3
"""Using spponacular API to get recipes based on ingredients"""
import re
import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.text import Text

# #loading the API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# Setting the API URL and params
spoonacular_url = "https://api.spoonacular.com/"


class Food:
    """Main Food class for all other methods"""

    def __init__(self):
        pass

    def cuisine(self, args):
        """Returns a list of recipes based on cuisine"""
        if args:
            cuisine = args[0]
            number = args[1]
        else:
            return "Please enter the cuisine and number of recipes"
        params = {
            "apiKey": api_key,
            "cuisine": cuisine,
            "number": number,
            "addRecipeInformation": True,
            "fillIngredients": True,
        }
        response = requests.get(
            spoonacular_url + "recipes/complexSearch", params=params)
        if response.status_code == 200:
            data = response.json()
            recipes = []
            for items in data["results"]:
                print(items["title"], items["id"], items["sourceUrl"])
                image = items["image"]
                if image is None:
                    print("No image")
                else:
                    if image.startswith('http'):
                        recipes.append(
                    (items["id"], items["title"], items["sourceUrl"], image))
                    else:
                        recipes.append(
                            (items["id"], items["title"], items["sourceUrl"]))            
            return recipes
        else:
            raise Exception(f"Error: {response.status_code}")

    def recipe(self, args):
        """Returns recipe details based on ingredient"""
        if args:
            recipe_id = args[0]
        else:
            return "Please enter the recipe ID"
        params = {"apiKey": api_key, "includeNutrition": True}
        response = requests.get(
            spoonacular_url + f"recipes/{recipe_id}/information", params=params)
        if response.status_code == 200:
            data = response.json()
            recipe_details = {}
            recipe_details["title"] = data["title"]
            recipe_details["image"] = data["image"]
            recipe_details["sourceUrl"] = data["sourceUrl"]
            recipe_details["summary"] = self._clean_html_tags(data["summary"])
            recipe_details["nutrients"] = data["nutrition"]["nutrients"]
            return recipe_details
        else:
            raise Exception(f"Error: {response.status_code}")
        
    def ingredients(self, args):
        """ get recipe details based on ingredient """
        if args:
            ingredient = args[0]
            number = args[1]
        else:
            return "Please enter the ingredient and number of recipes"
        params = {"apiKey": api_key, "query": ingredient, "number": number}
        response = requests.get(spoonacular_url + "recipes/complexSearch", params=params)
        if response.status_code == 200:
            data = response.json()
            recipes = []
            for items in data["results"]:
                image = items["image"]
                if image is None or not image.startswith('http'):
                    recipes.append(
                        (items["id"], items["title"], items["sourceUrl"]))
                if image.startswith('http'):
                        recipes.append(
                            (items["id"], items["title"], items["sourceUrl"], image))
            return recipes
        else:
            raise Exception(f"Error: {response.status_code}")
    
    def random(self, args):
        """returns a list of random recipes"""
        if args:
            number = args[0]
        else:
            number = 1
        params = {"apiKey": api_key, "number": number}
        response = requests.get(
            spoonacular_url + "recipes/random", params=params)
        if response.status_code == 200:
            data = response.json()
            recipes = []
            for items in data["recipes"]:
                image = items["image"]
                if image:
                    if image.startswith('http'):
                        recipes.append(
                            (items["id"], items["title"], items["sourceUrl"], image))
                        print(recipes)
            return recipes
        else:
            print('Error:', response.status_code)
        
    def image(self, args):
        """get recipe image"""
        if args:
            ingredient = args[0]
            number = args[1]
        else:
            return "Please enter the recipe ID"
        params = {"apiKey": api_key, "query": ingredient, "number": number}
        response = requests.get(spoonacular_url + f"recipes/{ingredient}/information", params=params)
        if response.status_code == 200:
            data = response.json()
            # return data["image"]
            image = data["image"]
            # show image on html page only if image source is not empty and starts with http
            if image and image.startswith("http"):
                the_image = requests.get(image)
                if the_image.status_code == 200:
                    with open("recipe_image.jpg", "wb") as f:
                        f.write(the_image.content)
                    return "recipe_image.jpg"
        else:
            raise Exception(f"Error: {response.status_code}")

    
    def summary (self, args):
        """get recipe summary"""
        if args:
            ingredient = args[0]
            number = args[1]
        else:
            return "Please enter the recipe ID"
        params = {"apiKey": api_key, "query": ingredient, "number": number}
        if ingredient in self.recipe:
                response = requests.get(spoonacular_url + f"recipes/{ingredient}/summary", params=params)
        else:
            return "Please enter a valid recipe"
        if response.status_code == 200:
            data = response.json()
            return data["summary"]
        else:
            raise Exception(f"Error: {response.status_code}")
        
    def equipment (self, args):
        """get recipe equipment"""
        if args:
            ingredient = args[0]
            number = args[1]
        else:
            return "Please enter the recipe ID"
        params = {"apiKey": api_key, "query": ingredient, "number": number}
        if ingredient in self.recipe:
                response = requests.get(spoonacular_url + f"recipes/{ingredient}/equipmentWidget.json", params=params)
        else:
            return "Please enter a valid recipe"
        if response.status_code == 200:
            data = response.json()
            return data["equipment"]
        else:
            raise Exception(f"Error: {response.status_code}")
        
    def nutrition(self, args):
        """get recipe nutrition"""
        if args:
            ingredient = args[0]
            number = args[1]
        else:
            return "Please enter the recipe ID"
        params = {"apiKey": api_key, "query": ingredient, "number": number}
        if ingredient in self.recipe:
                response = requests.get(spoonacular_url + f"recipes/{ingredient}/nutritionWidget.json", params=params)
        else:
            return "Please enter a valid recipe"
        if response.status_code == 200:
            data = response.json()
            return data["nutrition"]
        else:
            raise Exception(f"Error: {response.status_code}")
         
    def _clean_html_tags(self, text):
        """Clean HTML tags from text"""
        clean = re.compile("<.*?>")
        return re.sub(clean, "", text)


if __name__ == "__main__":
    food = Food()
    # print(food.cuisine("african", 5))
    # print(food.query("chicken", 5))
    # print(food.recipe(716429))
    # print(food.ingredient("chicken", 5))
    # print(food.random(5))
    # print(food.summary(716429))
    # print(food.equipment(716429))
    # print(food.nutrition(716429))
# Usage Example:
# food = Food()
# print(food.cuisine("african", 5))