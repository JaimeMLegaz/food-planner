import pickle


class IngredientList:

    def __init__(self, filename="ingredients"):
        self.ingredients = []
        self.filename = filename

    # Checks extensively if two lists of ingredients are equal (same elements and order)
    def extensive_eq(self, list2):
        list1 = self.ingredients
        list1.sort()
        list2.sort()
        equality = True
        for i in range(len(list1)):
            equality = equality and list1[i].extensive_eq(list2[i])
        return equality

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, new_filename):
        self._filename = new_filename

    def add_ingredient(self, new_ing):
        self.ingredients.append(new_ing)

    # Saves the list to a file
    def save_ingredients(self):
        outfile = open(self.filename, "wb")
        pickle.dump(self.ingredients, outfile)
        outfile.close()

    # Loads the ingredients from a file
    @staticmethod
    def read_ingredients_file(filename):
        try:
            infile = open(filename, "rb")
            new_list = pickle.load(infile)
            infile.close()
            return new_list
        except(OSError, IOError) as e:
            return []

    def load_ingredients(self):
        self.ingredients = self.read_ingredients_file(self.filename)