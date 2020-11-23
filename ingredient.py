class Ingredient:

    def __init__(self, name, calories, carbs, proteins, fats):
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.proteins = proteins
        self.fat = fats

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @property
    def calories(self):
        return self.calories

    @calories.setter
    def calories(self, new_calories):
        self.calories = new_calories

    @property
    def proteins(self):
        return self.proteins

    @proteins.setter
    def proteins(self, new_prot):
        self.proteins = new_prot

    @property
    def carbs(self):
        return self.carbs

    @carbs.setter
    def carbs(self, new_carbs):
        self.carbs = new_carbs

    @property
    def fat(self):
        return self.fat

    @fat.setter
    def fat(self, new_fat):
        self.fat = new_fat

