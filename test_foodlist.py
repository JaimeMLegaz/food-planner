from unittest import TestCase
from foodlist import FoodList
from food import Food
from ingredient import Ingredient


class TestFoodList(TestCase):

    list = FoodList()

    def test_add_food(self):
        old_size = len(self.list.food)
        empty_food = Food("empty")
        self.list.add_food(empty_food)
        self.assertEqual(old_size + 1, len(self.list.food))

    def test_read_food_file(self):
        self.list.save_food()
        new_list = self.list.read_food_file(self.list.filename)
        old_list = self.list.food
        self.assertTrue(new_list == old_list)


