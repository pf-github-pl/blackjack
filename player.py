from hand import Hand, HandOverflow


class Player:
    def __init__(self, role):
        self.role = role
        self.hand = Hand()

    def get_cards(self, card):
        self.hand.cards.append(card)
        self.hand.value += card.value
        if card.figure == 'A' and len([card.figure for card in self.hand.cards if card.figure == 'A']) > 1:
            self.hand.value -= 10
        if self.hand.value > 21:
            raise HandOverflow

    def show_one_card(self):
        return f'{self.role} ma {self.hand.cards[1]}'

    def show_hand(self):
        return f'{self.role} ma {self.hand.cards}'
