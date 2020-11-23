import pickle


class FoodList:

    def __init__(self, filename="foods"):
        self.food = []
        self.filename = filename

    def add_food(self, new_food):
        self.food.append(new_food)

    def save_food(self):
        outfile = open(self.filename, "wb")
        pickle.dump(self.food, outfile)
        outfile.close()

    @staticmethod
    def read_food_file(filename):
        infile = open(filename, "rb")
        new_list = pickle.load(infile)
        infile.close()
        return new_list

    def load_food(self):
        self.food = self.read_food_file(self.filename)

