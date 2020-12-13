import tkinter as tk
from functools import partial
from foodlist import FoodList


class Windows:

    def __init__(self, foodlist, ingredientlist):
        self.food_list = foodlist
        self.ingredient_list = ingredientlist

    def add_food(self, food_entry):
        print("Adding " + food_entry.get())

    def remove_food(self):
        print("Remove food")

    @staticmethod
    def window_main():
        window = tk.Tk()
        window.title("Food Planner")

        for i in range(3):
            print(i)
            window.columnconfigure(i, weight=1)

        for i in range(2):
            window.rowconfigure(i, weight=1)

        f1 = tk.Frame(master=window)
        f1.grid(row=0, column=1)

        f2 = tk.Frame(master=window)
        f2.grid(row=1, column=0, padx=20, pady=10)

        f3 = tk.Frame(master=window)
        f3.grid(row=1, column=1, pady=10)

        f4 = tk.Frame(master=window)
        f4.grid(row=1, column=2, padx=20, pady=10)

        txt = tk.Label(master=f1, text="Select your next action", height=7)
        but1 = tk.Button(master=f2, text="Add food", width=20)
        but2 = tk.Button(master=f3, text="Plan meals", width=20)
        but3 = tk.Button(master=f4, text="Add ingredient", width=20)
        txt.pack()
        but1.pack()
        but2.pack()
        but3.pack()
        return window

    def win_add_food(self):
        window = tk.Tk()
        window.title("Food Planner")

        window.rowconfigure(4, minsize=20)
        window.resizable(False, False)

        # Middle frame
        frame2 = tk.Frame(master=window)
        frame2.grid(column=2, row=1)

        # Content of left frame
        listbox_left = tk.Listbox()
        for food in self.food_list.food:
            listbox_left.insert(tk.END, food.name)
        listbox_left.grid(column=1, row=1, rowspan=4, pady=15, padx=10)

        # Content of middle frame
        entry = tk.Entry(frame2)
        entry.grid(column=2, row=1, padx=(0, 10), pady=(11, 10))

        # Buttons' functionality
        button_add = partial(self.add_food, entry)
        button_remove = partial(self.remove_food, entry)

        # Buttons of middle frame
        button_add = tk.Button(frame2, text="Add", command=button_add)
        button_remove = tk.Button(frame2, text="Delete", command=button_remove)
        button_add.grid(column=2, row=2, pady=(0, 10))
        button_remove.grid(column=2, row=3, pady=(0, 10))

        # Content of left frame
        listbox_right = tk.Listbox()
        for food in self.food_list.food:
            listbox_right.insert(tk.END, food.name)
        listbox_right.grid(column=3, row=1, rowspan=4, pady=15, padx=10)

        return window

    def ingredients_win(self):
        window = tk.Tk()
        window.title("Adding Ingredient")

        lab_title = tk.Label(window, text="List of Ingredients")
        list_ing = tk.Listbox()
        for ing in self.ingredient_list.ingredients:
            list_ing.insert(tk.END, ing.name)
        but_remove = tk.Button(window, text="Remove Ingredient")
        but_add = tk.Button(window, text="Add Ingredient")

        lab_title.grid(column=1, row=1, columnspan=2, pady=10)
        list_ing.grid(column=1, row=2, rowspan=3, columnspan=2)
        but_remove.grid(column=1, row=5, padx=10, pady=10)
        but_add.grid(column=2, row=5, padx=(0, 10), pady=10)

        return window

    def add_ingredient_win(self):
        window = tk.Tk()
        window.title("New Ingredient")

        lab_title = tk.Label(window, text="Adding new Ingredient")
        entry_names = ["Name", "Calories/100gr", "Carbs/100gr", "Proteins/100gr", "Fats/100gr"]

        lab_title.grid(column=1, columnspan=2, row=1, pady=(5, 5))
        row_num = 2
        for name in entry_names:
            label = tk.Label(window, text=name)
            label.grid(column=1, row=row_num, padx=(10, 2), sticky="E")

            ent = tk.Entry(window)
            ent.grid(column=2, row=row_num, padx=(2, 10))

            row_num += 1

        add_button = tk.Button(window, text="Add")
        add_button.grid(column=1, row=row_num, columnspan=2, pady=(5, 10))

        return window
