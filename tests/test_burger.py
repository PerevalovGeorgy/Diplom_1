import pytest
from praktikum.database import Database
from data_for_test import Data
from praktikum.burger import Burger
from praktikum.bun import Bun


class TestBurger:
    def test_set_test_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.get_name() == Data.name_bun

    def test_add_test_ingredient(self, ingredient_1):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        assert burger.ingredients[0].get_name() == Data.name_ingredient_1

    def test_add_two_ingredients_and_remove_one_ingredient(self, ingredient_1, ingredient_2):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1

    def test_move_test_ingredients(self, ingredient_1, ingredient_2):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].get_name() == Data.name_ingredient_2

    def test_get_price_test_burger(self, bun, ingredient_1, ingredient_2):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.get_price() == 700

    def test_get_receipt_test_burger(self, bun, ingredient_1, ingredient_2):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert '700' in burger.get_receipt()
