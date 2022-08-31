import itertools
from random import shuffle


class HandOverflow(Exception):
    def __str__(self):
        return '<<< PRZEKROCZONO 21. GRA SKOŃCZONA! >>>'


class Card:
    def __init__(self, figure, color):
        self.figure = figure
        self.color = color
        self.value = self.assign_value(figure)

    @staticmethod
    def assign_value(figure):
        if figure == 'A':
            return 11
        elif figure in ['K', 'J', 'Q']:
            return 10
        elif figure in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return int(figure)
        else:
            raise ValueError

    def __str__(self):
        return f'{self.figure} {self.color}'

    def __repr__(self):
        return f'{self.figure} {self.color}'


class Deck:
    def __init__(self):
        self.cards = self.create()

    @staticmethod
    def create():
        cards = []
        figures = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        colors = ['pik', 'trefl', 'kier', 'karo']
        for figure, color in itertools.product(figures, colors):
            cards.append(Card(figure, color))
        return cards

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop(-1)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0


class Player:
    def __init__(self, role):
        self.role = role
        self.hand = Hand()

    def get_cards(self, card):
        self.hand.cards.append(card)
        self.hand.value += card.value
        if self.hand.value > 21:
            raise HandOverflow

    def show_one_card(self):
        return f'{self.role} ma {self.hand.cards[1]}'

    def show_hand(self):
        return f'{self.role} ma {self.hand.cards}'


class Game:
    def __init__(self):
        self.croupier = Player('Krupier')
        self.player = Player('Gracz')
        self.deck = Deck()

    def get_decision(self):
        return input('Co chcesz zrobić (H - dobierz, S - stój): ').upper() == 'H'

    def play(self):
        self.deck.shuffle()
        self.croupier.get_cards(self.deck.draw())
        self.croupier.get_cards(self.deck.draw())
        self.player.get_cards(self.deck.draw())
        self.player.get_cards(self.deck.draw())

        print(self.croupier.show_one_card())
        print(self.player.show_hand())

        while True:
            decision = self.get_decision()
            if decision:
                try:
                    next_card = self.deck.draw()
                    self.player.get_cards(next_card)
                    print(self.player.show_hand())
                    if self.player.hand.value == 21:
                        break
                except HandOverflow as exception:
                    print(exception)
                    break
            else:
                break

        while self.player.hand.value > self.croupier.hand.value and self.player.hand.value < 21:
            try:
                next_card = self.deck.draw()
                self.croupier.get_cards(next_card)
            except HandOverflow as exception:
                print(exception)
                break

        print(self.croupier.show_hand())
        print(self.player.show_hand())

        if self.player.hand.value > self.croupier.hand.value and self.player.hand.value <= 21:
            print(f'Brawo wygrałeś {self.player.hand.value} do {self.croupier.hand.value}!')
        elif self.player.hand.value == self.croupier.hand.value and self.player.hand.value <= 21:
            print(f'Remis {self.player.hand.value} do {self.croupier.hand.value}')
        elif self.player.hand.value < self.croupier.hand.value and self.croupier.hand.value > 21:
            print(f'Brawo wygrałeś {self.player.hand.value} do {self.croupier.hand.value}!')
        else:
            print(f'Przegrałeś {self.player.hand.value} do {self.croupier.hand.value}.')

        print(f'Po rozdaniu w talii pozostało {len(self.deck.cards)} kart.')


if __name__ == '__main__':
    Game().play()
