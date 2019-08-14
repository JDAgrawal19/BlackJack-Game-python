from Dealer import Dealer
from Cards import Cards
from Player import Player


class Table(object):

    def __init__(self, number_of_decks, number_of_players, name_of_players):
        self.dealer = Dealer()
        self.players = [Player(name) for name in name_of_players]
        self.cards = Cards(number_of_decks)

    def distribute_card_to_dealer(self):
        self.dealer.hand.append(self.cards.take_a_card_from_stack())

    def distribute_card_to_player(self, player):
        player.hand.append(self.cards.take_a_card_from_stack())

    def show_first_card_of_dealer(self):
        return {self.dealer.name: self.dealer.hand[0]}

    def show_cards_of_players(self):
        return {player.name: player.hand for player in self.players}

    def calc_score(self, player_or_dealer):
        player_or_dealer.score = 0
        player_or_dealer.value_for_ace_card = 11
        for card_key, card_value in player_or_dealer.hand:
            if card_key == 'A':
                player_or_dealer.score += player_or_dealer.value_for_ace_card
            else:
                player_or_dealer.score += card_value
        if player_or_dealer.score > 21 and ('A', None) in player_or_dealer.hand:
            player_or_dealer.score -= 10
            player_or_dealer.value_for_ace_card = 1
        return player_or_dealer.score

    def get_the_results_of_game(self):
        results = []
        for player in self.players:
            if self.dealer.score > 21 and player.score <= 21:
                results.append({'dealer': 'Loser', player.name: 'Winner'})
            elif (player.score > 21) or (21 > self.dealer.score > player.score):
                results.append({'dealer': 'Winner', player.name: 'Loser'})
            elif self.dealer.score < 21 and self.dealer.score < player.score:
                results.append({'dealer': 'Loser', player.name: 'Winner'})
            elif self.dealer.score == player.score == 21 and \
                    len(self.dealer.hand) == 2 and len(player.hand) > 2:
                results.append({'dealer': 'Winner', player.name: 'Loser'})
            elif self.dealer.score == player.score == 21 \
                    and len(self.dealer.hand) > 2 and len(player.hand) == 2:
                results.append({'dealer': 'Loser', player.name: 'Winner'})
            elif (self.dealer.score == player.score == 21 and
                  len(self.dealer.hand) == 2 and len(player.hand) == 2) \
                    or (self.dealer.score == player.score):
                results.append({'dealer': 'Push', player.name: 'Push'})
        return results




