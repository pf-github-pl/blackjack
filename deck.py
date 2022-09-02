from random import shuffle
import itertools

from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for figure, color in itertools.product(Card.card_figures, Card.card_colors):
            self.cards.append(Card(figure, color))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop(-1)
