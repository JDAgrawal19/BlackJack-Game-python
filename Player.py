class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.value_for_ace_card = 11

    def check_if_player_says_hit(self, choice):
        if choice.lower() == 'hit':
            return True
        elif choice.lower() == 'stand':
            return False

    def check_if_player_is_busted(self):
        if self.score > 21:
            return True
        else:
            return False
