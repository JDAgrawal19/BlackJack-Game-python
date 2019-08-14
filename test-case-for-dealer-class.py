import unittest
from Dealer import Dealer


class DealerTester(unittest.TestCase):
    def test_if_name_is_correct(self):
        d = Dealer()
        self.assertEqual(True, d.name == "Nick")

    def test_if_score_is_zero_on_initialization(self):
        d = Dealer()
        self.assertEqual(0, d.score)

    def test_if_hand_is_empty_on_initialization(self):
        d = Dealer()
        self.assertEqual(0, len(d.hand))

    def test_value_for_ace_card_on_initialization(self):
        d = Dealer()
        self.assertEqual(11, d.value_for_ace_card)


if __name__ == '__main__':
    unittest.main()
