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

    def load_food(self):
        infile = open(self.filename, "rb")
        new_food = pickle.load(infile)
        print(new_food == self.food)
        infile.close()

