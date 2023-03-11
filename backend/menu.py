#!/usr/bin/python3

"""
this is the main menu for the app
"""
from food import Food
# from wildlife import Wildlife
# from music import Music


class Menu:
    """main menu class"""
    def __init__(self):
        pass

    def main_menu(self):
        """main menu"""
        name = input("what is your name? ")
        print("Hello", name)
        print("Thank you for using our app and welcome to greatness")
        print("This app is designed to help you find recipes of foods you like")
        print("The main menu has 2 options")
        print("main menu")
        print("\t Food")
        print("\t Exit")
        ans = str(input("Do you really want to know about food and recipes? \n answer should be yes or no ")).lower()
        if ans == 'yes':
            print('welcome to the food menu')
            print('you can now use the methods in the Food class')
            print('1. Cuisine')
            print('2. Ingredients')
            print('1. Cuisine')
            print('2. Ingredients')
            print('3. nutrition')
            print('4. summary')
            print('5. image')
            print('6. random')
            # print('7. instructions')
            print('7. go back to main menu')
            print('8. exit')
            ans2 = int(input("Enter the number of the parameter you want to use: "))
            food = Food()
            if ans2 in range(1, 10):
                if ans2 == 1:
                    food.Cuisine()
                elif ans2 == 2:
                    food.ingredients()
                elif ans2 == 3: 
                    food.nutrition()
                elif ans2 == 4:
                    food.summary()
                elif ans2 == 5:
                    food.image()
                elif ans2 == 6:
                    food.random()
                # elif ans2 == 7:
                    # food.instructions()
                elif ans2 == 7:
                    print('go back to main menu')
                    self.main_menu()
                elif ans2 == 8:
                    print('exit')
                else:
                    print("Invalid input \n Valid options are 1, 2, 3, 4, 5, 6, 7, 8 \ntry again")
                    self.main_menu()
        elif ans == 'no':
            print(f"Goodbye {name}.\nThank you for using our app")    
        else:
            self.main_menu()

menu = Menu() # create an instance of the class
menu.main_menu() # this is the main menu