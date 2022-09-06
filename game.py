from deck import Deck
from player import Player
from hand import HandOverflow


class GameOverPlayerException(Exception):
    def __str__(self):
        return 'PRZEGRAŁEŚ! Przekroczyłeś 21'


class GameOverCroupierException(Exception):
    def __str__(self):
        return 'WYGRAŁEŚ! Krupier przekroczył 21'


class Game:
    def __init__(self):
        self.croupier = Player('Krupier')
        self.player = Player('Gracz')
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _get_decision():
        return input('Co chcesz zrobić (0 - dobierz kartę, 1 - stój): ')

    def user_plays(self):
        while True:
            decision = self._get_decision()
            if decision:
                try:
                    self.player.get_cards(self.deck.draw())
                    print(self.player.show_hand())
                except HandOverflow as exception:
                    raise exception
            else:
                break

    def croupier_plays(self):
        while self.player.hand.value > self.croupier.hand.value:
            try:
                self.croupier.get_cards(self.deck.draw())
            except HandOverflow as exception:
                raise exception


    def play(self):
        self.croupier.get_cards(self.deck.draw())
        self.croupier.get_cards(self.deck.draw())
        self.player.get_cards(self.deck.draw())
        self.player.get_cards(self.deck.draw())

        print(self.croupier.show_one_card())
        print(self.player.show_hand())

        try:
            self.user_plays()
        except HandOverflow as exception:
            print(self.croupier.show_hand())
            print(self.player.show_hand())
            raise GameOverPlayerException from exception

        try:
            self.croupier_plays()
        except HandOverflow as exception:
            print(self.croupier.show_hand())
            print(self.player.show_hand())
            raise GameOverCroupierException from exception
        print(self.croupier.show_hand())
        print(self.player.show_hand())

        if self.player.hand.value > self.croupier.hand.value:
            print(f'Brawo wygrałeś {self.player.hand.value} do {self.croupier.hand.value}!')
        elif self.player.hand.value == self.croupier.hand.value:
            print(f'Remis {self.player.hand.value} do {self.croupier.hand.value}')
        elif self.player.hand.value < self.croupier.hand.value:
            print(f'Przegrywasz {self.player.hand.value} do {self.croupier.hand.value}!')