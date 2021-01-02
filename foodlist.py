import pickle


class FoodList:

    def __init__(self, filename="foods"):
        self.food = []
        self.filename = filename

    def extensive_eq(self, list2):
        list1 = self.food
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

    def add_food(self, new_food):
        self.food.append(new_food)
        self.save_food()

    def remove_food(self, index):
        del self.food[index]
        self.save_food()

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


