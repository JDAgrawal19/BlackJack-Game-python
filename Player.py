class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []
        self.value_for_ace_card = 11

    def check_if_player_is_busted(self):
        return self.score > 21
