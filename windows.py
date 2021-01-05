import tkinter as tk
from functools import partial
from foodlist import FoodList
from ingredient import Ingredient
from food import Food
import tkinter.font as font
import re


class Windows:

    def __init__(self, foodlist, ingredientlist):
        self.food_list = foodlist
        self.ingredient_list = ingredientlist
        self.window = self.base_window()

        # List of available frames this window will use
        self.frames = {"ings": self.ingredients_win(self.window),
                       "foods": self.food_win(self.window),
                       "add_food": self.add_food_win(self.window),
                       "add_ing": self.add_ingredient_win(self.window),
                       "main": self.main_win(self.window),
                       "food_list_ing": self.food_list_of_ingredients(self.window, None),
                       "edit_ing_prop": self.edit_ing_proportions_win(self.window)}

        self.current_frame = self.frames["main"]
        self.current_frame.grid(column=0, row=0)

    # Replaces the current frame
    def goto_page(self, page_name):
        self.current_frame.grid_remove()
        self.current_frame = self.frames[page_name]
        self.current_frame.grid(column=0, row=0)

    def filter_search_food(self, chosen_ings, food_name_entry, search_entry):
        # Change window to the same but with the args
        self.frames["add_food"] = self.add_food_win(self.window, chosen_ings, food_name_entry, search_entry.get())
        self.goto_page("add_food")

    def filter_ingredients(self, search_entry):
        self.frames["ings"] = self.ingredients_win(self.window, search_entry.get())
        self.goto_page("ings")

    # TODO: PASS NOT ONLY THE INDEX BUT BOTH LISTS, CHECK THE INDEX IN THE FULL LIST FOR THE ITEM CHOSEN,
    # AND THEN APPLY THE OLD METHODS FOR REMOVAL, USING THE INDEX NOT THE ITEM. REMOVE THE EXTENSIVE_EQ METHOD
    def remove_food(self, food):
        if food.curselection():
            self.food_list.remove_food(food.curselection()[0])  # TODO Add method
        # Refresh the frame
        self.frames["foods"] = self.food_win(self.window)
        self.goto_page("foods")

    def base_window(self):
        window = tk.Tk()
        window.title("FoodPlanner")
        return window

    # Adds an ingredient to the list and updates it
    def add_ingredient(self, name, calories, carbs, proteins, fats):
        new_ingredient = Ingredient(name.get(), calories.get(), carbs.get(), proteins.get(), fats.get())
        self.ingredient_list.add_ingredient(new_ingredient)
        # Refresh the frame
        self.frames["ings"] = self.ingredients_win(self.window)
        self.goto_page("ings")

    def remove_ingredient(self, ingredient, filtered_list):
        if ingredient.curselection():
            if len(self.ingredient_list.ingredients) > len(filtered_list):
                filtered_ing_index = ingredient.curselection()[0]
                selected_ing = filtered_list[filtered_ing_index]
                selected_ing_index = self.ingredient_list.ingredients.index(selected_ing)
            else:
                selected_ing_index = ingredient.curselection()[0]

            self.ingredient_list.remove_ingredient(selected_ing_index)
        # Refresh the frame
        self.frames["ings"] = self.ingredients_win(self.window)
        self.goto_page("ings")

    # TODO: Do the same treatment for this as for the ingredients removal
    def add_food_ingredients(self, ingredient, chosen_ingredients, filtered_list, food_name):
        if ingredient.curselection():
            if len(self.ingredient_list.ingredients) > len(filtered_list):
                filtered_ing_index = ingredient.curselection()[0]
                selected_ing = filtered_list[filtered_ing_index]
                selected_ing_index = self.ingredient_list.ingredients.index(selected_ing)
            else:
                selected_ing_index = ingredient.curselection()[0]

            new_ing = self.ingredient_list.ingredients[selected_ing_index]
            chosen_ingredients.append(new_ing)
            # Refresh the frame
            self.frames["add_food"] = self.add_food_win(self.window, chosen_ingredients, food_name)
            self.goto_page("add_food")

    def add_food(self, food_name, ingredients):
        if food_name.get() and (len(ingredients) >= 1):
            new_food = Food(food_name.get())
            for ingredient in ingredients:
                new_food.add_ingredient(ingredient)

            # Update the frame
            self.frames["food_list_ing"] = self.food_list_of_ingredients(self.window, new_food)
            self.goto_page("food_list_ing")
        else:
            print("NONAME")

    def ingredients_win(self, window, search_filter=None):
        frame = tk.Frame(window)

        lab_title = tk.Label(frame, text="List of Ingredients")

        filtered_ing_list = [ing.name for ing in self.ingredient_list.ingredients]
        if search_filter:
            r = re.compile(".*" + search_filter + ".*")
            filtered_ing_list = list(filter(r.match, filtered_ing_list))

        list_ing = tk.Listbox(frame, width=43)
        for ing in filtered_ing_list:
            list_ing.insert(tk.END, ing)
        but_remove = tk.Button(frame, text="Remove Ingredient", command=partial(self.remove_ingredient, list_ing,
                                                                                filtered_ing_list), width=17)

        scrollbar = tk.Scrollbar(frame)
        list_ing.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=list_ing.yview)

        but_add = tk.Button(frame, text="Add Ingredient", command=partial(self.goto_page, "add_ing"), width=17)

        lab_title.grid(column=1, row=1, columnspan=3, pady=10)
        list_ing.grid(column=1, row=2, rowspan=3, columnspan=2, padx=(10, 0))
        scrollbar.grid(column=3, row=2, rowspan=3, sticky="wns", padx=(0, 10))

        frame2 = tk.Frame(frame)
        frame2.grid(column=1, columnspan=3, row=5)
        search_entry = tk.Entry(frame2, width=35)
        search_button = tk.Button(frame2, text="Search", command=partial(self.filter_ingredients, search_entry))
        search_entry.grid(column=1, row=5, columnspan=2, sticky="e")
        search_button.grid(column=3, row=5, sticky="w")

        but_remove.grid(column=1, row=6, padx=10, pady=5, sticky="w")
        but_add.grid(column=2, columnspan=2, row=6, padx=(0, 10), pady=5, sticky="e")

        button_back = tk.Button(frame, text="Back", width=41, command=partial(self.goto_page, "main"))
        button_back.grid(column=1, columnspan=3, row=7, sticky="ew", pady=(0, 10), padx=10)

        return frame

    def main_win(self, window):
        frame = tk.Frame(window)

        for i in range(3):
            frame.columnconfigure(i, weight=1)

        for i in range(2):
            frame.rowconfigure(i, weight=1)

        f1 = tk.Frame(master=frame)
        f1.grid(row=0, column=1)

        f2 = tk.Frame(master=frame)
        f2.grid(row=1, column=0, padx=20, pady=10)

        f3 = tk.Frame(master=frame)
        f3.grid(row=1, column=1, pady=10)

        f4 = tk.Frame(master=frame)
        f4.grid(row=1, column=2, padx=20, pady=10)

        txt = tk.Label(master=f1, text="Select your next action", height=7)
        but1 = tk.Button(master=f2, text="Add food", width=20, command=partial(self.goto_page, "foods"))
        but2 = tk.Button(master=f3, text="Plan meals", width=20)
        but3 = tk.Button(master=f4, text="Add ingredient", width=20, command=partial(self.goto_page, "ings"))
        txt.pack()
        but1.pack()
        but2.pack()
        but3.pack()
        return frame

    def food_win(self, window):
        frame = tk.Frame(window)
        lab_title = tk.Label(frame, text="List of Foods")
        list_food = tk.Listbox(frame, width=28)
        for food in self.food_list.food:
            list_food.insert(tk.END, food.name)
        but_remove = tk.Button(frame, text="Remove Food", command=partial(self.remove_food, list_food))

        but_add = tk.Button(frame, text="Add Food", command=partial(self.goto_page, "add_food"))

        lab_title.grid(column=1, row=1, columnspan=2, pady=10)
        list_food.grid(column=1, row=2, rowspan=3, columnspan=2)
        but_remove.grid(column=1, row=5, padx=10, pady=10)
        but_add.grid(column=2, row=5, padx=(0, 10), pady=10)

        button_back = tk.Button(frame, text="Back", width=24, command=partial(self.goto_page, "main"))
        button_back.grid(column=1, columnspan=2, row=6, sticky="ew", pady=(0, 10), padx=10)

        return frame

    def add_food_win(self, window, chosen_ings=None, food_name=None, search_filter=None):
        if chosen_ings is None:
            chosen_ings = []

        frame = tk.Frame(window)

        lab_title = tk.Label(frame, text="Select the ingredients of the food")
        lab_title.grid(row=1, column=1, columnspan=4, pady=10)

        food_name_lab = tk.Label(frame, text="Name of the food")
        food_name_lab.grid(row=2, column=1, sticky="W", padx=10)
        food_name_entry = tk.Entry(frame, width=82)
        if food_name:
            food_name_entry.insert(0, food_name.get())
        food_name_entry.grid(row=3, column=1, columnspan=4, sticky="W", padx=10, pady=(0, 5))

        all_ing_lab = tk.Label(frame, text="All ingredients")
        all_ing_lab.grid(row=4, column=1, padx=(10, 5))

        selected_ing_lab = tk.Label(frame, text="Selected ingredients")
        selected_ing_lab.grid(row=4, column=4, padx=(5, 10))

        filtered_ing_list = [ing.name for ing in self.ingredient_list.ingredients]
        if search_filter:
            r = re.compile(".*" + search_filter + ".*")
            filtered_ing_list = list(filter(r.match, filtered_ing_list))

        all_ing_list = tk.Listbox(frame, width=33)
        for ing in filtered_ing_list:
            all_ing_list.insert(tk.END, ing)
        all_ing_list.grid(row=5, column=1, padx=(10, 0), pady=(0, 5))
        scrollbar1 = tk.Scrollbar(frame)
        all_ing_list.config(yscrollcommand=scrollbar1.set)
        scrollbar1.config(command=all_ing_list.yview)
        scrollbar1.grid(row=5, column=2, padx=(0, 5), sticky="wns")

        add_ingredient_button = tk.Button(frame, text="->", command=partial(self.add_food_ingredients, all_ing_list,
                                                                            chosen_ings, filtered_ing_list,
                                                                            food_name_entry))
        add_ingredient_button.grid(row=5, column=3)

        selected_ing_list = tk.Listbox(frame, width=33)
        for ing in chosen_ings:
            selected_ing_list.insert(tk.END, ing.name)
        selected_ing_list.grid(row=5, column=4, padx=(5, 0), pady=(0, 5))
        scrollbar2 = tk.Scrollbar(frame)
        selected_ing_list.config(yscrollcommand=scrollbar2.set)
        scrollbar2.config(command=selected_ing_list.yview)
        scrollbar2.grid(row=5, column=5, padx=(0, 10), sticky="wns")

        search_frame = tk.Frame(frame)
        search_entry = tk.Entry(search_frame, width=20)
        search_entry.grid(row=1, column=2, ipady=3)
        search_frame.grid(row=6, column=1, pady=(0, 10))  # TODO Make search work with removal
        search_button = tk.Button(search_frame, text="Search", command=partial(self.filter_search_food, chosen_ings,
                                                                               food_name_entry, search_entry))
        search_button.grid(row=1, column=1)

        frame2 = tk.Frame(frame)
        frame2.grid(row=6, column=4)
        next_button = tk.Button(frame2, text="Next", width=12, command=partial(self.add_food, food_name_entry,
                                                                               chosen_ings))
        next_button.grid(row=1, column=1, pady=(0, 10), padx=(6, 8))

        cancel_button = tk.Button(frame2, text="Cancel", width=12, command=partial(self.goto_page, "foods"))
        cancel_button.grid(row=1, column=2, pady=(0, 10))

        return frame

    def add_ingredient_win(self, window):
        frame = tk.Frame(window)

        lab_title = tk.Label(frame, text="Adding new Ingredient")
        entry_names = ["Name", "Calories/100gr", "Carbs/100gr", "Proteins/100gr", "Fats/100gr"]
        entries = {}

        lab_title.grid(column=1, columnspan=2, row=1, pady=5)
        row_num = 2
        for name in entry_names:
            label = tk.Label(frame, text=name)
            label.grid(column=1, row=row_num, padx=(10, 2), sticky="E")

            ent = tk.Entry(frame)
            ent.grid(column=2, row=row_num, padx=(2, 10))
            entries[name] = ent

            row_num += 1

        add_button = tk.Button(frame, text="Add", command=partial(self.add_ingredient, entries["Name"],
                                                                  entries["Calories/100gr"],
                                                                  entries["Carbs/100gr"],
                                                                  entries["Proteins/100gr"],
                                                                  entries["Fats/100gr"]), width=15)

        add_button.grid(column=1, row=row_num, padx=12, pady=(5, 10), sticky="w")

        cancel_button = tk.Button(frame, text="Cancel", command=partial(self.goto_page, "ings"), width=15)
        cancel_button.grid(column=2, row=row_num, padx=12, pady=(5, 10), sticky="e")

        return frame

    def to_edit_ing_prop(self, window, ingredient, new_food):
        if ingredient.curselection():
            self.frames["edit_ing_prop"] = self.edit_ing_proportions_win(window, ingredient.curselection()[0], new_food)
            self.goto_page("edit_ing_prop")


    def food_list_of_ingredients(self, window, new_food):
        frame = tk.Frame(window)

        if new_food is not None:
            lab_title = tk.Label(frame, text="Edit ingredients' proportions of " + new_food.name)
            lab_title.grid(row=1, column=1, columnspan=2, padx=10, pady=(10, 5))

            ing_list = tk.Listbox(frame, width=35)
            for ing in new_food.ingredients:
                ing_list.insert(tk.END, ing.name)
            ing_list.grid(row=2, column=1, pady=(0, 5), padx=(10, 0))

            scrollbar = tk.Scrollbar(frame)
            ing_list.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=ing_list.yview)
            scrollbar.grid(row=2, column=2, sticky="wns", pady=(0, 5), padx=(0, 10))

            edit_button = tk.Button(frame, text="Edit ingredient", width=30,
                                    command=partial(self.to_edit_ing_prop, window, ing_list, new_food))
            edit_button.grid(row=3, column=1, columnspan=2, pady=(0, 5))
            finish_button = tk.Button(frame, text="Finish", width=30)
            finish_button.grid(row=4, column=1, columnspan=2, pady=(0, 10))
            finish_button.config(height=2)

        return frame

    def edit_ing_proportions_win(self, window, ingredient_index=None, food=None):
        frame = tk.Frame(window)

        if food:
            ingredient = food.ingredients[ingredient_index]
            min_ration = food.minimums[ingredient.name]
            max_ration = food.maximums[ingredient.name]

            lab_title = tk.Label(frame, text=ingredient.name)
            lab_title.config(font=("Courier, 13"))
            lab_title.grid(column=1, columnspan=2, row=1, pady=(10, 0))

            lab_subtitle = tk.Label(frame, text="Ration for one person")
            lab_subtitle.grid(column=1, columnspan=2, row=2, pady=(0, 5))

            lab_min = tk.Label(frame, text="Minimum acceptable amount (gr)")
            lab_min.grid(column=1, row=3, padx=(10, 0))
            lab_max = tk.Label(frame, text="Maximum acceptable amount (gr)")
            lab_max.grid(column=1, row=4, padx=(10, 0), pady=(0, 10))

            entry_min = tk.Entry(frame)
            entry_min.insert(0, min_ration)
            entry_min.grid(column=2, row=3, padx=(0, 10))
            entry_max = tk.Entry(frame)
            entry_max.insert(0, max_ration)
            entry_max.grid(column=2, row=4, padx=(0, 10), pady=(0, 10))

            save_button = tk.Button(frame, text="Save", width=20)
            save_button.grid(column=1, columnspan=2, row=5, pady=(0, 10))

        return frame
