#!/usr/bin/python3
"""Using spponacular API to get recipes based on ingredients"""
import os
import json
import requests
# import random
from PIL import Image
from io import BytesIO
from rich.console import Console
from rich.text import Text
from dotenv import load_dotenv

#loading the API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# setting the API url and params
spoonacular_url = "https://api.spoonacular.com/"

params_list = {"apiKey": api_key, "cuisine": "african", "type": "main course",}


class Food:
    """main food class for all other methods"""
    
    def __init__(self):
        pass
    
    def Cuisine(self, *args):
        """returns a list of recipes based on cuisine"""
        if args:
            cuisine = args[0]
            number = args[1]
        else:
            return "Please enter the cuisine and number of recipes"
        params = {"apiKey": api_key, "cuisine": cuisine, "number": number, "addRecipeInformation": True, "fillIngredients": False}
        response = requests.get(spoonacular_url + "recipes/complexSearch", params=params)
        if response.status_code == 200:
            data = response.json()
            for y, i in enumerate(data['results']):
                """prints the recipes but not on console"""
                return y+1, i['title']
        else:
            print('Error:', response.status_code)
                # time.sleep(.5)

    def query(self, *args):
        """returns a list of recipes based on query"""
        if args:
            query = args[0]
            number = args[1]
            params = {"apiKey": api_key, "query": query, "number": number, "addRecipeInformation": True, "fillIngredients": False}
            response = requests.get(spoonacular_url + "recipes/complexSearch", params=params)
            if response.status_code == 200:
                data = response.json()
                for y, i in enumerate(data['results']):
                    return (y+1, i['title'])
            else:
                print('Error:', response.status_code)
        else:
            return "Please enter the query and number of recipes"

    def ingredients(self, *args):
        if args:
            ingredients = args[0]
            number = args[1]
            number = input("Enter the number of recipes: ")
            params = {"apiKey": api_key, "query": ingredients, "number": number, "includeIngredients": True, "addRecipeInformation": True}
            response = requests.get(spoonacular_url + "recipes/complexSearch?", params=params)
            if response.status_code == 200:
                data = response.json()
                # print(response.url)
                for y, x in enumerate(data['results']):
                    the_title = Text(f"{y+1}. {x['title']}")
                    the_title.stylize("bold red")
                    Console().print(the_title)
                    for keys in x['analyzedInstructions']:
                        for z in keys['steps']:
                            print(z['number'])
                            print('\t', z['step'])
                            for item in z['ingredients']:
                                 return ("\t", 'ingredient:', item['name'])
            else:
                print('Error:', response.status_code)
        else:
            return "Please enter the ingredients and number of recipes"
    
    def random(self, *args): 
        """returns a list of recipes"""
        if args:
            number = args[0]
        else:
            number = 1
        params = {"apiKey": api_key, "number": number}
        response = requests.get(spoonacular_url + "recipes/random", params=params)
        if response.status_code == 200:
            data = response.json()
            for i in data['recipes']:
                print(i['title'])
                # print(i['image'])
                image =  requests.get(i['image'])
                photo = Image.open(BytesIO(image.content))
                photo.show()
                for keys in i['analyzedInstructions']:
                    for z in keys['steps']:
                        print(z['number'])
                        print('\t', z['step'])
                        for item in z['ingredients']:
                            return ("\t", 'ingredient:', item['name'])
        else:
            return ('Error:', response.status_code)
            
    def nutrition(self, *args):
        """returns the nutrition of a recipe"""
        if args:
            recipe = args[0]
            number = args[1]
        else:
            return "Please enter the recipe and number of recipes"
        params = {"apiKey": api_key, "query": recipe, "number": number, "addRecipeInformation": True, "fillIngredients": False}
        response = requests.get(spoonacular_url + "recipes/complexSearch?", params=params)
        if response.status_code == 200:
            data = response.json()
            for i in data['results']:
                print(i['title'])
                score = Text(f"Health Score: {i['healthScore']}")
                return score.stylize("bold red")
        else:
            return ('Error:', response.status_code)
    
    def summary(self, *args):
        """returns the summary of a recipe"""
        if args:
            recipe = args[0]
            number = args[1]
        else:
            number = 1
            return "Please enter the recipe and number of recipes"
        params = {"apiKey": api_key, "recipe": recipe, "number": number, "addRecipeInformation": True, "fillIngredients": False}
        response = requests.get(spoonacular_url + "recipes/complexSearch?", params=params)
        if response.status_code == 200:
            data = response.json()
            for y, i in enumerate(data['results']):
                print(y+1, i['title'])
                for char in i['summary']:
                    if char == '.' or char == '!' or char == '?':
                        # go to next line and print the next sentence
                        char.replace(char, '.\n')  # replace the punctuation with a new line
                        # add > to the beginning of the new line
                        char.replace(char, '>\t')  # replace the punctuation with a new line
                        return char  # print the new line
                    else:
                        print(char, end='') # print the rest of the sentence
        else:
            return 'Error:', response.status_code
            
    def image(self, *args): 
        """returns the image of a recipe"""
        if args:
            recipe = args[0]
            number = args[1]
        else:
            number = 1
            return "Please enter the recipe"
        # recipe = input("Enter the recipe: ")
        # number = input("Enter the number of recipes: ")
        params = {"apiKey": api_key, "query": recipe, "number": number}
        response = requests.get(spoonacular_url + "recipes/complexSearch?", params=params)
        if response.status_code == 200:
            data = response.json()
            # print(json.dumps(data, indent=4, sort_keys=True, separators=(',', ': ')))
            # print(data)
            # print(response.url)
            for i in data['results']:
                print(i['title'])
                if i['image'] == '':
                    print('No image available')
                elif 'https' in i['image']:
                    image = requests.get(i['image'])
                    photo = Image.open(BytesIO(image.content))
                    photo.show()
                else:
                    image = requests.get('https://' + i['image'])
                    photo = Image.open(BytesIO(image.content))
                    photo.show()
        else:
            print('Error:', response.status_code)


if __name__ == "__main__":
    food = Food()
    # food.Cuisine()
    # food.ingredients()
    # food.random()
    # food.nutrition()
    # food.image()
    # food.summary()
    
    