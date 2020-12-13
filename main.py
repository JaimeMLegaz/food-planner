from ingredient import Ingredient
from food import Food
from foodlist import FoodList
from ingredientlist import IngredientList
from windows import Windows
import pickle
import easygui as ui
import tkinter as tk

food_list = FoodList()
ingredient_list = IngredientList()
windows = Windows(food_list, ingredient_list)

# Step 1: Load the food list
food_list.load_food()  # In case there is no food list, an empty list gets loaded
ingredient_list.load_ingredients()

# Step 2: Starting the main loop and showing the options to the user
win = windows.add_ingredient_win()
win.mainloop()








