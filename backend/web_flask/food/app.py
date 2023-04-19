#!/usr/bin/python3
"""rendering the html pages of food app"""

from flask import Flask, render_template, request
from api import Food
import requests


app = Flask(__name__)
food = Food()

route = '/africandelights/'
@app.route(route) # this is the home page
def home():
    return render_template('menu.html')

@app.route(route, methods=['POST'])
def get_recipe():
    # this is the method selected from the drop down menu
    method = request.form.get('method')
    if method == 'random':  # (number)
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = [number]
        randoms = food.random(args)
        for item in randoms:
            titles = item['title']
            print(titles)
            urls = item['url']
            print(urls)
            images = item['image']
        return render_template('menu.html', randoms=randoms, titles=titles, urls=urls, images=images)
    
    elif method == 'Cuisine':  # (cuisine, number)
        # Perform recipe search logic with args
        cuisine = request.form['cuisine'] # this is the cuisine entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = [cuisine, number]  # this is the cuisine entered in the text box
        cuisines = food.cuisine(args)
        for item in cuisines:
            title = item['title']
            url = item['url']
            image = item['image']
        return render_template('menu.html', cuisines=cuisines, title=title, url=url, image=image)

    elif method == 'ingredients':  # (ingredients, number)
        ingredients = request.form['ingredients'] # this is the recipe entered in the text box
        number = request.form['number'] # this is the number of recipes entered in the text box
        args = (ingredients, number)
        rengredients = food.ingredients(args)
        for item in rengredients:
            title = item['title']
            url = item['url']
            image = item['image']
            health = item['health']
            hscore = item['nutrition']
        return render_template('menu.html', rengredients=rengredients, title=title, url=url, image=image, health=health, hscore=hscore)

    else:
        return "No method selected"

@app.route('/africandelights/contacts')
def template():
    """rendering the contact page"""
    return render_template('contact.html')

@app.route('/africandelights/about')
def template1():
    """rendering the about page"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
