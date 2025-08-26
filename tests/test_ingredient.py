import pytest
from praktikum.ingredient import Ingredient
from data import DataForTest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, DataForTest.filling_name, DataForTest.filling_price)
        assert ingredient.get_name() == DataForTest.filling_name

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, DataForTest.sauce_name, DataForTest.sauce_price)
        assert ingredient.get_price() == DataForTest.sauce_price

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            (INGREDIENT_TYPE_FILLING, DataForTest.filling_name, DataForTest.filling_price),
            (INGREDIENT_TYPE_SAUCE, DataForTest.sauce_name, DataForTest.sauce_price)
        ]
    )
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
