import collections


class Food:

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.minimums = {}
        self.maximums = {}
        self.optionals = []

    #  self.proportions = {}

    def __eq__(self, other):
        return self.name == other.name

    def extensive_eq(self, other):
        equality = True
        equality = equality and (self.name == other.name)
        equality = equality and (collections.Counter(self.ingredients) == collections.Counter(other.ingredients))
        equality = equality and (self.minimums == other.minimums)
        equality = equality and (self.maximums == other.maximums)
        equality = equality and (collections.Counter(self.optionals) == collections.Counter(other.optionals))
        return equality

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def add_ingredient(self, ingredient, minimum, maximum, optional=False):
        self.ingredients.append(ingredient)
        self.minimums[ingredient.name] = minimum
        self.maximums[ingredient.name] = maximum
        if optional:
            self.optionals.append(ingredient.name)

    def min_values(self):
        calories = 0
        carbs = 0
        proteins = 0
        fats = 0

        for ingredient in self.ingredients:
            name = ingredient.name
            calories = calories + ingredient.calories
            carbs = carbs + (ingredient.carbs * self.minimums[name] / 100)
            proteins = proteins + (ingredient.proteins * self.minimums[name] / 100)
            fats = fats + (ingredient.fats * self.minimums[name] / 100)

        return calories, carbs, proteins, fats

    def max_values(self):
        calories = 0
        carbs = 0
        proteins = 0
        fats = 0

        for ingredient in self.ingredients:
            name = ingredient.name
            calories = calories + ingredient.calories
            carbs = carbs + (ingredient.carbs * self.maxmimums[name] / 100)
            proteins = proteins + (ingredient.proteins * self.maxmimums[name] / 100)
            fats = fats + (ingredient.fats * self.maxmimums[name] / 100)

        return calories, carbs, proteins, fats
