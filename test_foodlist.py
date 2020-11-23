from unittest import TestCase
from foodlist import FoodList
from food import Food
from ingredient import Ingredient


class TestFoodList(TestCase):

    list = FoodList()

    def test_add_food(self):
        old_size = len(self.list.food)
        banana_split = Food("banana_split")  # So that the food that we compare have at least two ingredients
        banana_ing = Ingredient("banana", 75, 60, 0, 5)
        banana_split.add_ingredient(banana_ing, 100, 100)
        cream_ing = Ingredient("cream", 190, 100, 10, 50)
        banana_split.add_ingredient(cream_ing, 25, 45, True)

        self.list.add_food(banana_split)  # We add the food to the list
        self.assertEqual(old_size + 1, len(self.list.food))  # We check if the list is bigger by one element

    def test_read_food_file(self):
        self.list.save_food()  # We save the current list (it counts the previous additions) to a file
        new_list = self.list.read_food_file(self.list.filename)  # We read it from the saved file
        old_list = self.list.food
        self.assertTrue(new_list == old_list)  # We compare both lists (only the names of the foods)

    def test_non_existing_food_file(self):
        empty_list = self.list.read_food_file("non_existing_file")
        self.assertEqual(empty_list, [])  # A non existing file should return an empty list

    def test_extensive_read_food_file(self):
        self.list.save_food()
        new_list = self.list.read_food_file(self.list.filename)
        self.assertTrue(self.list.extensive_eq(new_list))  # Same as comparing two lists, but comparing everything
