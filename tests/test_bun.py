import pytest
from praktikum.database import Database
from data_for_test import Data
from praktikum.burger import Burger
from praktikum.bun import Bun


class TestBun:
    def test_get_name_test_bun(self, bun):
        assert bun.get_name() == Data.name_bun

    def test_get_price_test_bun(self, bun):
        assert bun.get_price() == Data.price_bun

