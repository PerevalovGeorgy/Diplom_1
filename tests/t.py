from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database
from praktikum.burger import Burger
from data_for_test import Data


bur = Burger()
vun = Bun(Data.name_bun, Data.price_bun)
vun.name = 's'
ing_1 = Ingredient(Data.type_ingredient_1, Data.name_ingredient_1, Data.price_ingredient_1)
ing_2 = Ingredient(Data.type_ingredient_2, Data.name_ingredient_2, Data.price_ingredient_2)
bur.add_ingredient(ing_1)
bur.add_ingredient(ing_2)
bur.set_buns(vun)
print(bur.get_receipt())
print(vun.name)

