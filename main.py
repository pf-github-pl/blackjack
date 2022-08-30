import itertools
from random import shuffle


class Card:
    def __init__(self, figure, color):
        self.figure = figure
        self.color = color
        self.value = self.assign_value(figure)

    @staticmethod
    def assign_value(figure):
        if figure in ['A', 'K', 'J', 'Q']:
            return 10
        elif figure in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return int(figure)
        else:
            raise ValueError

    def __str__(self):
        return f'Karta: {self.figure} koloru: {self.color} ma wartość: {self.value}'

    def __repr__(self):
        return f'{self.figure} {self.color}'


class Deck:
    def __init__(self):
        self.cards = []

    def create(self):
        figures = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        colors = ['pik', 'trefl', 'kier', 'karo']
        for figure, color in itertools.product(figures, colors):
            self.cards.append(Card(figure, color))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop(-1)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def get_cards(self, card):
        if self.value + card.value > 21:
            raise HandOverflow
        else:
            self.cards.append(card)
            self.value += card.value


class Croupier:
    def __init__(self, hand):
        self.hand = hand


class Player:
    def __init__(self, hand):
        self.hand = hand


class HandOverflow(Exception):
    pass


def play():
    new_deck = Deck()
    new_deck.create()
    new_deck.shuffle()

    croupier_hand = Hand()
    croupier = Croupier(croupier_hand)
    croupier_hand.get_cards(new_deck.draw())
    croupier_hand.get_cards(new_deck.draw())

    player_hand = Hand()
    player = Player(player_hand)
    player_hand.get_cards(new_deck.draw())
    player_hand.get_cards(new_deck.draw())

    print(f'Krupier ma: {croupier.hand.cards[:1]}')
    print(f'Gracz ma {player.hand.cards}')

    decision = input('Co chcesz zrobić (H - dobierz, S - stój): ')
    while decision.upper() == 'H':
        try:
            card = new_deck.draw()
            player_hand.get_cards(card)
        except HandOverflow as exception:
            print(card)
            print(f'Niestety przegrywasz! {exception}')
            raise

        print(player.hand.cards)
        decision = input('Co chcesz zrobić (H - dobierz, S - stój): ')

    while player.hand.value > croupier.hand.value:
        try:
            croupier_hand.get_cards(new_deck.draw())
        except HandOverflow:
            print(card)
            print('Krupier przegrywa!')
            print(f'Karty krupiera to: {croupier.hand.cards}')
            print(f'Twoje karty to: {player.hand.cards}')
            raise

    print(f'Karty krupiera to: {croupier.hand.cards}')
    print(f'Twoje karty to: {player.hand.cards}')

    if player.hand.value > croupier.hand.value:
        print(f'Brawo wygrałeś {player.hand.value} do {croupier.hand.value}!')
    elif player.hand.value == croupier.hand.value:
        print(f'Remis {player.hand.value} do {croupier.hand.value}')
    else:
        print(f'Przegrana {player.hand.value} do {croupier.hand.value}.')

    print(f'Po rozdaniu w talii pozostało {len(new_deck.cards)} kart.')


if __name__ == '__main__':
    play()