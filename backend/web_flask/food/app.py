#!/usr/bin/python3
"""rendering the html pages of food app"""

import requests
from flask import Flask, render_template, request
from flask import Flask, render_template, request, url_for
from api import Food


app = Flask(__name__)
food = Food()

route = '/africandelights/'
@app.route(route) # this is the home page
def home():
    return render_template('menu.html')

# method should be selected from the drop down menu in html
# route += method + '/' # this is the route for the method selected
@app.route(route, methods=['POST'])
def get_recipe():
    # this is the method selected from the drop down menu
    method = request.form.get('method')
    if method == 'random':  # (number)
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = [number]
        result = food.random(args)
        
    elif method == 'Cuisine':  # (cuisine, number)
        # Perform recipe search logic with args
        cuisine = request.form['cuisine'] # this is the cuisine entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = [cuisine, number]  # this is the cuisine entered in the text box
        # print(args)
        result = food.cuisine(args)
        print(result)
        
    elif method == 'ingredients':  # (ingredients, number)
        ingredients = request.form['ingredients'] # this is the recipe entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (ingredients, number)
        result = food.ingredients(args)
        
    elif method == 'image':  # (ingredient, number)
        ingredients = request.form['ingredients'] # this is the recipe entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (ingredients, number)
        result = food.image(args)
        
    elif method == 'nutrition':  # (ingredients, number)
        ingredients = request.form['ingredients'] # this is the recipe entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (ingredients, number)
        result = food.nutrition(args)
        
    elif method == 'summary':  # (ingredients, number)
        ingredients = request.form['ingredients']
        number = request.form['number']
        args = (ingredients, number)
        result = food.summary(args)
        
    elif method == 'equipment':  # (ingredients, number)
        ingredients = request.form['ingredients']
        number = request.form['number']
        args = (ingredients, number)
        result = food.equipment(args)
        
    elif method == 'recipe':  # (recipe_id, number)
        recipe_id = request.form['recipe_id']
        number = request.form['number']
        args = (recipe_id, number)
        result = food.recipe(args)
 
    else:
        result = "No method selected"
    # string_result = str(result)
    return render_template('menu.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
