from praktikum.bun import Bun
from data import DataForTest


class TestBun:
    def test_get_name(self):
        bun = Bun(DataForTest.bun_name, DataForTest.bun_price)
        assert bun.get_name() == DataForTest.bun_name

    def test_get_price(self):
        bun = Bun(DataForTest.bun_name, DataForTest.bun_price)
        assert bun.get_price() == DataForTest.bun_price
