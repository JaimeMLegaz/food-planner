from unittest import TestCase
from foodlist import FoodList
from food import Food
from ingredient import Ingredient


class TestFoodList(TestCase):

    list = FoodList()

    def test_add_food(self):
        old_size = len(self.list.food)
        banana = Food("banana")
        banana_ing = Ingredient("banana", 75, 60, 0, 5)
        banana.add_ingredient(banana_ing, 100, 100)
        self.list.add_food(banana)
        self.assertEqual(old_size + 1, len(self.list.food))

    def test_read_food_file(self):
        self.list.save_food()
        new_list = self.list.read_food_file(self.list.filename)
        old_list = self.list.food
        self.assertTrue(new_list == old_list)

    def test_non_existing_food_file(self):
        empty_list = self.list.read_food_file("non_existing_file")
        self.assertEqual(empty_list, [])

    def test_extensive_read_food_file(self):
        self.list.save_food()
        new_list = self.list.read_food_file(self.list.filename)
        self.assertTrue(self.list.extensive_eq(new_list))
