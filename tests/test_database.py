import pytest
from praktikum.database import Database
from data_for_test import Data
from praktikum.burger import Burger
from praktikum.bun import Bun


class TestDatabase:
    def test_available_buns_have_3_bun(self):
        bun = Database()
        assert len(bun.available_buns()) == 3

    def test_available_ingredients_have_6_ingredients(self):
        ingredient = Database()
        assert len(ingredient.available_ingredients()) == 6

