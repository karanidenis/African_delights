#!/usr/bin/python3
"""Using spponacular API to get recipes based on ingredients"""
# import os
import json
import requests
# import random
import time
from PIL import Image
from io import BytesIO
from rich.console import Console
from rich.text import Text
# import colorama
# from dotenv import load_dotenv

#loading the API key from .env file
# load_dotenv()
# api_key = os.getenv("API_KEY")
api_key = "8c824703899e461a83c284dbe5656f8d"
# print(api_key)

# setting the API url and params
spoonacular_url = "https://api.spoonacular.com/"
# params = {"apiKey": api_key, "cuisine": "african"}

params_list = {"apiKey": api_key, "cuisine": "african", "type": "main course",}


class Food:
    """main food class for all other methods"""
    
    def __init__(self):
        pass
    
    def Cuisine(self):
        """returns a list of recipes based on cuisine"""
        # diet = input("Enter the type of diet: ")
        cuisine = input("Enter the type of cuisine: ")
        number = int(input("Enter the number of recipes: "))
        params = {"apiKey": api_key, "cuisine": cuisine, "number": number, "addRecipeInformation": True, "fillIngredients": False}
        response = requests.get(spoonacular_url + "recipes/complexSearch", params=params)
        if response.status_code == 200:
            data = response.json()
            # print(json.dumps(data, indent=4, sort_keys=True, separators=(',', ': ')))
            # print(data)
            # print(response.url)
            print('This is what you get when you search for {}:'.format(cuisine))
            # for y in range(number):
                # for i in data['results']:
                #     print(y, i['title'])
            for y, i in enumerate(data['results']):
                print(y+1, i['title'])
                time.sleep(.5)
        else:
            print('Error:', response.status_code)
                # time.sleep(.5)

    def query(self): 
        query = input("Enter the type of meal: ")
        number = input("Enter the number of recipes: ")
        params = {"apiKey": api_key, "query": query, "number": number, "addRecipeInformation": True, "fillIngredients": False}
        response = requests.get(spoonacular_url + "recipes/complexSearch", params=params)
        if response.status_code == 200:
            data = response.json()
            # print(json.dumps(data, indent=4, sort_keys=True, separators=(',', ': ')))
            # print(data)
            for y, i in enumerate(data['results']):
                print(y+1, i['title'])
                time.sleep(.5)
        else:
            print('Error:', response.status_code)
    
    def ingredients(self):
        # ingredients = input("Enter the ingredients: ")
        query = input("Enter the type of meal: ")
        number = input("Enter the number of recipes: ")
        params = {"apiKey": api_key, "query": query, "number": number, "includeIngredients": True, "addRecipeInformation": True}
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
                            print("\t", 'ingredient:', item['name'])
                time.sleep(.5)
        else:
            print('Error:', response.status_code)
    
    def random(self): 
        """returns a list of recipes"""
        params = {"apiKey": api_key, "number": 1}
        response = requests.get(spoonacular_url + "recipes/random", params=params)
        if response.status_code == 200:
            data = response.json()
            # print(json.dumps(data, indent=4, sort_keys=True, separators=(',', ': ')))
            # print(data)
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
                            print("\t", 'ingredient:', item['name'])
                time.sleep(.5)
        else:
            print('Error:', response.status_code)
            
    def nutrition(self):
        """returns the nutrition of a recipe"""
        recipe = input("Enter the recipe: ")
        number = input("Enter the number of recipes: ")
        params = {"apiKey": api_key, "query": recipe, "number": number, "addRecipeInformation": True, "fillIngredients": False}
        response = requests.get(spoonacular_url + "recipes/complexSearch?", params=params)
        if response.status_code == 200:
            data = response.json()
            # print(json.dumps(data, indent=4, sort_keys=True, separators=(',', ': ')))
            # print(data)
            # print(response.url)
            for i in data['results']:
                print(i['title'])
                score = Text(f"Health Score: {i['healthScore']}")
                score.stylize("bold green")
                Console().print(score)
                time.sleep(.5)
        else:
            print('Error:', response.status_code)
    
    def summary(self):
        """returns the summary of a recipe"""
        recipe = input("Enter the recipe: ")
        number = input("Enter the number of recipes: ")
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
                        print(char)  # print the new line
                        time.sleep(.5)
                    else:
                        print(char, end='') # print the rest of the sentence
                time.sleep(.5)
        else:
            print('Error:', response.status_code)
            
    def image(self): 
        """returns the image of a recipe"""
        recipe = input("Enter the recipe: ")
        number = 2
        params = {"apiKey": api_key, "query": recipe, "number": number}
        response = requests.get(spoonacular_url + "recipes/complexSearch?", params=params)
        if response.status_code == 200:
            data = response.json()
            # print(json.dumps(data, indent=4, sort_keys=True, separators=(',', ': ')))
            # print(data)
            # print(response.url)
            for i in data['results']:
                print(i['title'])
                # print(i['image'])
                time.sleep(.5)
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
    food.summary()
    
    