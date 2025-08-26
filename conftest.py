import pytest

from unittest.mock import Mock
from data import DataForTest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = DataForTest.bun_name
    bun.get_price.return_value = DataForTest.bun_price
    return bun


@pytest.fixture
def mock_ingredient_1():
    ingredient1 = Mock()
    ingredient1.get_name.return_value = DataForTest.filling_name
    ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient1.get_price.return_value = DataForTest.filling_price
    return ingredient1


@pytest.fixture
def mock_ingredient_2():
    ingredient2 = Mock()
    ingredient2.get_name.return_value = DataForTest.sauce_name
    ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient2.get_price.return_value = DataForTest.sauce_price
    return ingredient2
