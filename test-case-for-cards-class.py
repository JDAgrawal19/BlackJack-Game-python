import unittest
from Cards import Cards


class CardTester(unittest.TestCase):
    def test_number_of_cards_when_number_of_decks_positive(self):
        c = Cards(3)
        self.assertEqual(156, len(c.stack))

    def test_number_of_cards_when_number_of_decks_zero(self):
        c = Cards(0)
        self.assertEqual(0, len(c.stack))

    def test_number_of_cards_when_number_decks_negative(self):
        c = Cards(-2)
        self.assertEqual(0, len(c.stack))


if __name__ == '__main__':
    unittest.main()
