from random import shuffle


class Cards(object):

    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.stack = [('A', None), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
                      ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                      ('J', 10), ('Q', 10), ('K', 10)] * 4 * self.number_of_decks
        self.shuffle()

    def shuffle(self):
        shuffle(self.stack)

    def take_a_card_from_stack(self):
        return self.stack.pop()
