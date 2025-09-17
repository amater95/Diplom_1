import pytest

from unittest.mock import Mock
from praktikum.burger import Burger
from data import DataForTest


class TestBurger:
    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is not None
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].get_type() == mock_ingredient_1.get_type()
        assert burger.ingredients[1].get_type() == mock_ingredient_2.get_type()
        assert burger.ingredients[0].get_name() == mock_ingredient_1.get_name()
        assert burger.ingredients[1].get_name() == mock_ingredient_2.get_name()
        assert burger.ingredients[0].get_price() == mock_ingredient_1.get_price()
        assert burger.ingredients[1].get_price() == mock_ingredient_2.get_price()

    def test_remove_ingredient(self, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == mock_ingredient_1.get_name()
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.ingredients[0].get_name() == mock_ingredient_1.get_name()
        assert burger.ingredients[1].get_name() == mock_ingredient_2.get_name()
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == mock_ingredient_2.get_name()
        assert burger.ingredients[1].get_name() == mock_ingredient_1.get_name()

    def test_get_price(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        assert burger.get_price() == DataForTest.burger_price_withouth_souce
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_price() == DataForTest.burger_price_with_2_ingredients
        
    def test_get_receipt(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        receipt = ("(==== Флюоресцентная булка R2-D3 ====)\n"
                   "= filling Плоды Фалленианского дерева =\n"
                   "= sauce Соус традиционный галактический =\n"
                   "(==== Флюоресцентная булка R2-D3 ====)\n"
                   "\n"
                   "Price: 2865")
        assert burger.get_receipt() == receipt
