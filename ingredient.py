class Ingredient:

    def __init__(self, name, calories, carbs, proteins, fats):
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.proteins = proteins
        self.fat = fats

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, new_calories):
        self._calories = new_calories

    @property
    def proteins(self):
        return self._proteins

    @proteins.setter
    def proteins(self, new_prot):
        self._proteins = new_prot

    @property
    def carbs(self):
        return self._carbs

    @carbs.setter
    def carbs(self, new_carbs):
        self._carbs = new_carbs

    @property
    def fat(self):
        return self._fat

    @fat.setter
    def fat(self, new_fat):
        self._fat = new_fat

