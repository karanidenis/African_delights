#!/usr/bin/python3
"""Using spponacular API to get recipes based on ingredients"""
import re
import os
import requests
# from dotenv import load_dotenv
# from rich.console import Console
# from rich.text import Text

# #loading the API key from .env file
# load_dotenv()
# api_key = os.getenv("API_KEY")
api_key = "8c824703899e461a83c284dbe5656f8d"

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
            # "fillIngredients": True,
        }
        response = requests.get(
            spoonacular_url + "recipes/complexSearch", params=params)
        # print(response.url) # for debugging
        resp_url = response.url
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
                        {'title': items["title"], 'url': items["sourceUrl"], 'image': image, 'resp_url': resp_url})
                    else:
                        recipes.append(
                        {'title': items["title"], 'url': items["sourceUrl"], 'resp_url': resp_url})
            return recipes
        else:
            raise Exception(f"Error: {response.status_code}")


    def ingredients(self, args):
        """ get recipe details based on ingredient """
        if args:
            ingredient = args[0]
            number = args[1]
        else:
            return "Please enter the ingredient and number of recipes"
        params = {"apiKey": api_key, "query": ingredient, "number": number, "addRecipeInformation": True, "fillIngredients": True, 'includeNutrition': True}
        response = requests.get(spoonacular_url + "recipes/complexSearch", params=params)
        if response.status_code == 200:
            data = response.json()
            recipes = []
            for items in data["results"]:
                image = items["image"]
                if image is None or not image.startswith('http'):
                    recipes.append(
                    {'title': items["title"], 'url': items["sourceUrl"], 'health': items['veryHealthy'], "nutrition": items["healthScore"]})
                if image.startswith('http'):
                        recipes.append(
                            {'title': items["title"], 'url': items["sourceUrl"], 'image': image, 'health': items['veryHealthy'], "nutrition": items["healthScore"]})
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
        resp_url = response.url
        if response.status_code == 200:
            data = response.json()
            recipes = []
            for items in data["recipes"]:
                image = items["image"]
                if image:
                    if image.startswith('http'):
                        recipes.append(
                            {'title': items["title"], 'url': items["spoonacularSourceUrl"], 'image': image, 'resp_url': resp_url})
            return recipes
        else:
            print('Error:', response.status_code)
         
    def _clean_html_tags(self, text):
        """Clean HTML tags from text"""
        clean = re.compile("<.*?>")
        return re.sub(clean, "", text)


if __name__ == "__main__":
    food = Food()
    # print(food.cuisine("african", 5))
    # print(food.ingredient("chicken", 5))
    # print(food.random(5))
# Usage Example:
# food = Food()
# print(food.cuisine("african", 5))