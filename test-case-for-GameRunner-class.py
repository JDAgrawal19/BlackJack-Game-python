import unittest
from GameRunner import GameRunner


class GameRunnerTester(unittest.TestCase):
    def test_when_number_of_decks_greater_than_eight(self):
        self.assertEqual(False, GameRunner.validate_no_of_decks(9))

    def test_when_number_of_decks_is_zero(self):
        self.assertEqual(False, GameRunner.validate_no_of_decks(0))

    def test_when_number_of_decks_is_negative(self):
        self.assertEqual(False, GameRunner.validate_no_of_decks(-2))

    def test_when_number_of_decks_is_five(self):
        self.assertEqual(True, GameRunner.validate_no_of_decks(5))

    def test_when_number_of_players_greater_than_ten(self):
        self.assertEqual(False, GameRunner.validate_no_of_players(11))

    def test_when_number_of_players_is_less_than_three(self):
        self.assertEqual(False, GameRunner.validate_no_of_players(2))

    def test_when_number_of_players_is_negative(self):
        self.assertEqual(False, GameRunner.validate_no_of_players(-2))

    def test_when_number_of_players_is_five(self):
        self.assertEqual(True, GameRunner.validate_no_of_players(5))


if __name__ == '__main__':
    unittest.main()
