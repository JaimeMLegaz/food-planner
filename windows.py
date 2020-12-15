import tkinter as tk
from functools import partial
from foodlist import FoodList
from ingredient import Ingredient


class Windows:

    def __init__(self, foodlist, ingredientlist):
        self.food_list = foodlist
        self.ingredient_list = ingredientlist
        self.window = self.base_window()

        self.frames = {"ings": self.ingredients_win(self.window),
                       "add_food": self.add_food_win(self.window),
                       "add_ing": self.add_ingredient_win(self.window),
                       "main": self.main_win(self.window)}

        self.current_frame = self.frames["main"]
        self.current_frame.grid(column=0, row=0)

    def goto_page(self, page_name):
        self.current_frame.grid_remove()
        self.current_frame = self.frames[page_name]
        self.current_frame.grid(column=0, row=0)

    def add_food(self, food_entry):
        print("Adding " + food_entry.get())

    def remove_food(self):
        print("Remove food")

    def base_window(self):
        window = tk.Tk()
        window.title("BaseWindow")
        return window

    def add_ingredient(self, name, calories, carbs, proteins, fats):
        new_ingredient = Ingredient(name.get(), calories.get(), carbs.get(), proteins.get(), fats.get())
        self.ingredient_list.add_ingredient(new_ingredient)
        self.frames["ings"] = self.ingredients_win(self.window)
        self.goto_page("ings")

    def remove_ingredient(self, ingredient):
        if ingredient.curselection():
            self.ingredient_list.remove_ingredient(ingredient.curselection()[0])
        self.frames["ings"] = self.ingredients_win(self.window)
        self.goto_page("ings")

    def ingredients_win(self, window):
        frame = tk.Frame(window)

        lab_title = tk.Label(frame, text="List of Ingredients")
        list_ing = tk.Listbox(frame)
        for ing in self.ingredient_list.ingredients:
            list_ing.insert(tk.END, ing.name)
        but_remove = tk.Button(frame, text="Remove Ingredient", command=partial(self.remove_ingredient, list_ing))

        but_add = tk.Button(frame, text="Add Ingredient", command=partial(self.goto_page, "add_ing"))

        lab_title.grid(column=1, row=1, columnspan=2, pady=10)
        list_ing.grid(column=1, row=2, rowspan=3, columnspan=2)
        but_remove.grid(column=1, row=5, padx=10, pady=10)
        but_add.grid(column=2, row=5, padx=(0, 10), pady=10)

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
        but1 = tk.Button(master=f2, text="Add food", width=20, command=partial(self.goto_page, "add_food"))
        but2 = tk.Button(master=f3, text="Plan meals", width=20)
        but3 = tk.Button(master=f4, text="Add ingredient", width=20, command=partial(self.goto_page, "ings"))
        txt.pack()
        but1.pack()
        but2.pack()
        but3.pack()
        return frame

    def add_food_win(self, window):
        frame = tk.Frame(window)

        frame.rowconfigure(4, minsize=20)

        # Middle frame
        frame2 = tk.Frame(master=frame)
        frame2.grid(column=2, row=1)

        # Content of left frame
        listbox_left = tk.Listbox(frame)
        for food in self.food_list.food:
            listbox_left.insert(tk.END, food.name)
        listbox_left.grid(column=1, row=1, rowspan=4, pady=15, padx=10)

        # Content of middle frame
        entry = tk.Entry(frame2)
        entry.grid(column=2, row=1, padx=(0, 10), pady=(11, 10))

        # Buttons' functionality
        button_add = partial(self.add_food, entry)
        button_remove = partial(self.remove_food)

        # Buttons of middle frame
        button_add = tk.Button(frame2, text="Add", command=button_add)
        button_remove = tk.Button(frame2, text="Delete", command=button_remove)
        button_add.grid(column=2, row=2, pady=(0, 10))
        button_remove.grid(column=2, row=3, pady=(0, 10))

        # Content of left frame
        listbox_right = tk.Listbox(frame)
        for food in self.food_list.food:
            listbox_right.insert(tk.END, food.name)
        listbox_right.grid(column=3, row=1, rowspan=4, pady=15, padx=10)

        return frame

    def add_ingredient_win(self, window):
        frame = tk.Frame(window)

        lab_title = tk.Label(frame, text="Adding new Ingredient")
        entry_names = ["Name", "Calories/100gr", "Carbs/100gr", "Proteins/100gr", "Fats/100gr"]
        entries = {}

        lab_title.grid(column=1, columnspan=2, row=1, pady=(5, 5))
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
                                                                  entries["Fats/100gr"]))

        add_button.grid(column=1, row=row_num, columnspan=2, pady=(5, 10))

        return frame
