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

    def test_save_food(self):
        self.fail()

    def test_load_food(self):
        self.fail()
