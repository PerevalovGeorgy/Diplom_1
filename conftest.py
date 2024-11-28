import pytest
from unittest.mock import Mock, patch
from praktikum.bun import Bun
from data_for_test import Data


@pytest.fixture
def bun():
    mok_bun = Mock()
    mok_bun.get_name.return_value = Data.name_bun
    mok_bun.get_price.return_value = Data.price_bun
    yield mok_bun


@pytest.fixture
def ingredient_1():
    mok_ingredient = Mock()
    mok_ingredient.get_name.return_value = Data.name_ingredient_1
    mok_ingredient.get_price.return_value = Data.price_ingredient_1
    mok_ingredient.get_type.return_value = Data.type_ingredient_1
    yield mok_ingredient


@pytest.fixture
def ingredient_2():
    mok_ingredient = Mock()
    mok_ingredient.get_name.return_value = Data.name_ingredient_2
    mok_ingredient.get_price.return_value = Data.price_ingredient_2
    mok_ingredient.get_type.return_value = Data.type_ingredient_2
    yield mok_ingredient

