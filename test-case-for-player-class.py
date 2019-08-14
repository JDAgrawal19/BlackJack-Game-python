import unittest
from Player import Player


class DealerTester(unittest.TestCase):
    def test_if_name_is_correct(self):
        d = Player('Jitesh')
        self.assertEqual('Jitesh', d.name)

    def test_if_score_is_zero_on_initialization(self):
        d = Player('Jitesh')
        self.assertEqual(0, d.score)

    def test_if_hand_is_empty_on_initialization(self):
        d = Player('Ajay')
        self.assertEqual(0, len(d.hand))

    def test_value_for_ace_card_on_initialization(self):
        d = Player('Ajay')
        self.assertEqual(11, d.value_for_ace_card)

    def test_player_is_busted(self):
        p = Player('Ajay')
        p.score = 22
        self.assertEqual(True, p.check_if_player_is_busted())

    def test_player_is_not_busted(self):
        p = Player('Jitesh')
        p.score = 21
        self.assertEqual(False, p.check_if_player_is_busted())


if __name__ == '__main__':
    unittest.main()
