import unittest

from shopping import shopping_basket


class Basket(unittest.TestCase):

    def test_that_there_is_a_shopping_basket(self):
        basket = shopping_basket.ShoppingBasket()
        self.assertIsNotNone(basket)

    def test_that_items_can_be_added_to_shopping_basket(self, items: str) -> None:
        basket = shopping_basket
        basket.add_item("Shoe")


if __name__ == '__main__':
    unittest.main()
