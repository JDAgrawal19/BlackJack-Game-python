import unittest
from Table import Table


class TableTester(unittest.TestCase):
    def test_card_added_in_dealer_hand(self):
        table = Table(2, 4)
        card = table.cards.stack[-1]
        table.distribute_card_to_dealer()
        self.assertEqual([card], table.dealer.hand)

    def test_two_cards_added_in_dealer_hand(self):
        table = Table(2, 4)
        cards = table.cards.stack[-1:-3:-1]
        table.distribute_card_to_dealer()
        table.distribute_card_to_dealer()
        self.assertEqual(cards, table.dealer.hand)

    def test_card_added_to_first_player_hand(self):
        table = Table(2, 4)
        cards = table.cards.stack[-1]
        table.distribute_card_to_player(table.players[0])
        self.assertEqual([cards], table.players[0].hand)

    def test_card_added_to_last_player_hand(self):
        table = Table(2, 4)
        cards = table.cards.stack[-1]
        table.distribute_card_to_player(table.players[-1])
        self.assertEqual([cards], table.players[-1].hand)

    def test_calculate_score_of_dealer_for_two_cards(self):
        table = Table(2, 4)
        cards = table.cards.stack[-1:-3:-1]
        table.distribute_card_to_dealer()
        table.distribute_card_to_dealer()
        score = cards[0][1] + cards[1][1]
        self.assertEqual(score, table.calc_score(table.dealer))

    def test_calculate_score_of_dealer_with_two_simple_cards_and_one_ace_card_and_cards_sum_exceeds_twenty_one(self):
        table = Table(2, 4)
        table.dealer.hand = [('10', 10), ('6', 6), ('A', None)]
        self.assertEqual(17, table.calc_score(table.dealer))

    def test_calculate_score_of_dealer_with_two_simple_cards_and_one_ace_card_and_card_sum_less_than_twenty_one(self):
        table = Table(2, 4)
        table.dealer.hand = [('4', 4), ('6', 6), ('A', None)]
        self.assertEqual(21, table.calc_score(table.dealer))

    def test_calculate_score_of_dealer_with_three_simple_cards(self):
        table = Table(2, 4)
        table.dealer.hand = [('10', 10), ('6', 6), ('7', 7)]
        self.assertEqual(23, table.calc_score(table.dealer))

    def test_results_of_game_when_dealer_is_busted(self):
        table = Table(2, 3)
        table.dealer.score = 23
        table.players[0].score = 20
        table.players[1].score = 22
        table.players[2].score = 21
        results = [{'dealer': 'Loser', 'player_1': 'Winner'}, {'dealer': 'Winner', 'player_2': 'Loser'},
                   {'dealer': 'Loser', 'player_3': 'Winner'}]
        self.assertEqual(results, table.get_the_results_of_game())

    def test_results_of_game_when_dealer_is_not_busted_and_score_of_dealer_and_player_is_different(self):
        table = Table(2, 4)
        table.dealer.score = 19
        table.players[0].score = 20
        table.players[1].score = 22
        table.players[2].score = 21
        table.players[3].score = 18
        results = [{'dealer': 'Loser', 'player_1': 'Winner'}, {'dealer': 'Winner', 'player_2': 'Loser'},
                   {'dealer': 'Loser', 'player_3': 'Winner'}, {'dealer': 'Winner', 'player_4': 'Loser'}]
        self.assertEqual(results, table.get_the_results_of_game())

    def test_results_of_game_when_dealer_has_blackjack_and_score_of_dealer_and_player_is_equal(self):
        table = Table(2, 3)
        table.dealer.hand = [('10', 10), ('A', None)]
        table.players[0].hand = [('10', 10), ('K', 10), ('A', None)]
        table.players[1].hand = [('10', 10), ('7', 7), ('4', 4)]
        table.players[2].hand = [('A', None), ('Q', 10)]
        table.dealer.score = 21
        table.players[0].score = 21
        table.players[1].score = 21
        table.players[2].score = 21
        results = [{'dealer': 'Winner', 'player_1': 'Loser'}, {'dealer': 'Winner', 'player_2': 'Loser'},
                   {'dealer': 'Push', 'player_3': 'Push'}]
        self.assertEqual(results, table.get_the_results_of_game())

    def test_results_of_game_when_dealer_has_no_blackjack_and_score_of_dealer_and_player_is_equal(self):
        table = Table(2, 3)
        table.dealer.hand = [('10', 10), ('K', 10), ('A', None)]
        table.players[0].hand = [('10', 10), ('K', 10), ('A', None)]
        table.players[1].hand = [('10', 10), ('7', 7), ('4', 4)]
        table.players[2].hand = [('A', None), ('Q', 10)]
        table.dealer.score = 21
        table.players[0].score = 21
        table.players[1].score = 21
        table.players[2].score = 21
        results = [{'dealer': 'Push', 'player_1': 'Push'}, {'dealer': 'Push', 'player_2': 'Push'},
                   {'dealer': 'Loser', 'player_3': 'Winner'}]
        self.assertEqual(results, table.get_the_results_of_game())

    def test_when_score_of_dealer_and_player_is_equal_and_none_have_blackjack(self):
        table = Table(2, 1)
        table.dealer.hand = [('10', 10), ('K', 10)]
        table.players[0].hand = [('10', 10), ('K', 10), ('A', None)]
        table.dealer.score = 20
        table.players[0].score = 20
        results = [{'dealer': 'Push', 'player_1': 'Push'}]
        self.assertEqual(results, table.get_the_results_of_game())


if __name__ == '__main__':
    unittest.main()
