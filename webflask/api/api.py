#!usr/bin/python3
"""creating african delights own food RESTapi"""

from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api
 
app = Flask(__name__)
api = Api(app)

@app.route('/africandelights/api/v1.0/recipes', methods=['POST'])
def create_recipe():
    if not request.json or not 'title' in request.json:
        abort(400)
    recipe = {
        'id': recipes[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    recipes.append(recipe)
    return jsonify({'recipe': recipe}), 201


@app.route('/africandelights/api/v1.0/recipes', methods=['GET'])
def get_recipes():
    recipes = [{ 'id': 1, 'title': 'Chicken and Chips', 'description': 'African style chicken and chips', 'done': False }]
    return jsonify({'recipes': recipes})
