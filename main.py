from ingredient import Ingredient
from food import Food
from foodlist import FoodList
import pickle
import easygui as ui

foodlist = FoodList()

# Step 1: Load the food list
foodlist.load_food()  # In case there is no food list, an empty list gets loaded

# Step 2: Starting the main loop and showing the options to the user
next_action = "Default"
while next_action:
    next_action = ui.buttonbox("Select the action", "Action select", ("Add ingredient", "Add food", "Plan my meal!"))









