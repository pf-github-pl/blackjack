from deck import Deck


class HandOverflow(Exception):
    def __str__(self):
        return '<<< PRZEKROCZONO 21. GRA SKOŃCZONA! >>>'


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
    play = True
    while play:
        Game().play()
        play = True if input('Chcesz grać dalej? [T/n] ').upper() != 'N' else False
