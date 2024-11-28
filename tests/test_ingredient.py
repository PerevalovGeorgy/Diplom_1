import pytest
from praktikum.database import Database
from data_for_test import Data
from praktikum.burger import Burger
from praktikum.bun import Bun


class TestIngredient:
    def test_get_name_test_ingredient(self, ingredient_1):
        assert ingredient_1.get_name() == Data.name_ingredient_1

    def test_get_price_test_ingredient(self, ingredient_1):
        assert ingredient_1.get_price() == Data.price_ingredient_1

    def test_get_type_test_ingredient(self, ingredient_1):
        assert ingredient_1.get_type() == Data.type_ingredient_1