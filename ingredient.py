class Ingredient:

    def __init__(self, name, calories, carbs, proteins, fats):
        self.name = name
        self.calories = calories
        self.carbs = carbs
        self.proteins = proteins
        self.fats = fats

    def __eq__(self, other):
        return((self.name == other.name) and
               (self.calories == other.calories) and
               (self.carbs == other.carbs) and
               (self.proteins == other.proteins) and
               (self.fats == other.fats))

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
    def fats(self):
        return self._fats

    @fats.setter
    def fats(self, new_fat):
        self._fats = new_fat

