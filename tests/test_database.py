from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_get_available_buns(self):
        available_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ]
        db = Database()
        db_buns = db.available_buns()
        assert len(db_buns) == len(available_buns)
        for i, bun in enumerate(db_buns):
            name, price = available_buns[i]
            assert bun.get_name() == name
            assert bun.get_price() == price

    def test_get_available_ingredients(self):
        available_ingredients = [
            ("hot sauce", INGREDIENT_TYPE_SAUCE, 100),
            ("sour cream", INGREDIENT_TYPE_SAUCE, 200),
            ("chili sauce", INGREDIENT_TYPE_SAUCE, 300),
            ("cutlet", INGREDIENT_TYPE_FILLING, 100),
            ("dinosaur", INGREDIENT_TYPE_FILLING, 200),
            ("sausage", INGREDIENT_TYPE_FILLING, 300),
        ]
        db = Database()
        db_ingredients = db.available_ingredients()
        assert len(db_ingredients) == len(available_ingredients)
        for i, ingredient in enumerate(db_ingredients):
            name, type_ing, price = available_ingredients[i]
            assert ingredient.get_name() == name
            assert ingredient.get_type() == type_ing
            assert ingredient.get_price() == price
