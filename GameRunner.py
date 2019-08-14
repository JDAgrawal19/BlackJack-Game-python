class GameRunner(object):
    @staticmethod
    def validate_no_of_decks(number_of_decks):
        if 1 <= number_of_decks <= 8:
            return True
        else:
            return False

    @staticmethod
    def validate_no_of_players(number_of_players):
        if 3 <= number_of_players <= 10:
            return True
        else:
            return False
