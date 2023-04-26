#!/usr/bin/python3
"""
Contains the MenuDocs classes
"""

import unittest
from unittest.mock import patch
from io import StringIO
from menu import Menu

class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()

    @patch('builtins.input', side_effect=['Alice', 'yes', 1, 8])
    def test_main_menu_food(self, mock_input):
        expected_output = ['what is your name? ', 'Hello Alice', 'Thank you for using our app and welcome to greatness',
                           'This app is designed to help you find recipes of foods you like', 'The main menu has 2 options',
                           'main menu', '\t Food', '\t Exit', 'Do you really want to know about food and recipes? \n answer should be yes or no ',
                           'welcome to the food menu', 'you can now use the methods in the Food class', '1. Cuisine',
                           '2. Ingredients', '1. Cuisine', '2. Ingredients', '3. nutrition', '4. summary', '5. image',
                           '6. random', '7. go back to main menu', '8. exit', 'Enter the number of the parameter you want to use: ',
                           'exit']
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.menu.main_menu()
            self.assertEqual(fake_output.getvalue().strip().split('\n'), expected_output)

    @patch('builtins.input', side_effect=['Bob', 'no'])
    def test_main_menu_exit(self, mock_input):
        expected_output = ['what is your name? ', 'Hello Bob', 'Thank you for using our app and welcome to greatness',
                           'This app is designed to help you find recipes of foods you like', 'The main menu has 2 options',
                           'main menu', '\t Food', '\t Exit', 'Do you really want to know about food and recipes? \n answer should be yes or no ',
                           'Goodbye Bob.\nThank you for using our app']
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.menu.main_menu()
            self.assertEqual(fake_output.getvalue().strip().split('\n'), expected_output)

    @patch('builtins.input', side_effect=['Cathy', 'yes', 9, 1, 'no'])
    def test_main_menu_invalid_input(self, mock_input):
        expected_output = ['what is your name? ', 'Hello Cathy', 'Thank you for using our app and welcome to greatness',
                           'This app is designed to help you find recipes of foods you like', 'The main menu has 2 options',
                           'main menu', '\t Food', '\t Exit', 'Do you really want to know about food and recipes? \n answer should be yes or no ',
                           'Invalid input \n Valid options are 1, 2, 3, 4, 5, 6, 7, 8 \ntry again', '1. Cuisine', '2. Ingredients',
                           '1. Cuisine', '2. Ingredients', '3. nutrition', '4. summary', '5. image', '6. random',
                           '7. go back to main menu', '8. exit', 'Enter the number of the parameter you want to use: ',
                           'Invalid input \n Valid options are 1, 2, 3, 4, 5, 6, 7, 8 \ntry again', 'Do you really want to know about food and recipes? \n answer should be yes or no ',
                           'Goodbye Cathy.\nThank you for using our app']
