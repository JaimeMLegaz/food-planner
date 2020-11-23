import pickle


class FoodList:

    def __init__(self, filename="foods"):
        self.food = []
        self.filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, new_filename):
        self._filename = new_filename

    def add_food(self, new_food):
        self.food.append(new_food)

    def save_food(self):
        outfile = open(self.filename, "wb")
        pickle.dump(self.food, outfile)
        outfile.close()

    @staticmethod
    def read_food_file(filename):
        try:
            infile = open(filename, "rb")
            new_list = pickle.load(infile)
            infile.close()
            return new_list
        except(OSError, IOError) as e:
            return []

    def load_food(self):
        self.food = self.read_food_file(self.filename)


