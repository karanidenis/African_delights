#!/usr/bin/python3
"""rendering the html pages of food app"""

from flask import Flask, render_template, request, url_for
from api import Food

app = Flask(__name__)
my_class = Food()

route = '/africandelights/'
@app.route(route) # this is the home page
def index():
    return render_template('homepage.html')

# method should be selected from the drop down menu in html
method = ''
# method = request.form['method'] # this is the method selected from the drop down menu
route += method + '/' # this is the route for the method selected

@app.route(route, methods=['GET'])  # this is the food page
def food():
    if method == 'ingredients':
        ingredients = request.form['ingredients'] # this is the recipe entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (ingredients, number)
        # use the api to get the recipes
        ingredients = my_class.ingredients(args)
        return render_template('menu.html', ingredients=ingredients) # this is the ingredients page

    if method == 'image':
        recipe = request.form['recipe'] # this is the recipe entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (recipe, number)
        image = my_class.image(args)
        return render_template('menu.html', recipe=recipe)
        
    if method == 'Cuisine':
        cuisine = request.form['cuisine'] # this is the cuisine entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (cuisine, number)
        # use the api to get the recipes
        recipe = my_class.Cuisine(args)
        return render_template('menu.html', recipe=recipe, number=number)
        
    if method == 'random':
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (number)
        # use the api to get the recipes
        rand_recipe = my_class.random(args)
        return render_template('menu.html', rand_recipe=rand_recipe)
        
    if method == 'nutrition':
        recipe = request.form['recipe'] # this is the recipe entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (recipe, number)
        # use the api to get the nutrition
        nutrition = my_class.nutrition(args)
        return render_template('menu.html', nutrition=nutrition, number=number)

    if method == 'summary':
        recipe = request.form['recipe']
        number = request.form['number']
        args = (recipe, number)
        # use the api to get the summary
        summary = my_class.summary(args)
        return render_template('menu.html', summary=summary, number=number)


@app.errorhandler(404)
def error(self):
    """error handler"""
    return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # this is the port for the app

# start the app with env variables set
# export FLASK_APP=app.py
# export FLASK_ENV=development
# python3 -m flask run