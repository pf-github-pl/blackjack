from deck import Deck
from card import Card

def test_creation():
    assert len(Deck().cards) == 52


def test_deck_colors():
    my_deck = Deck()
    assert len([card for card in my_deck.cards if card.color == 'pik']) == 13
    assert len([card for card in my_deck.cards if card.color == 'trefl']) == 13
    assert len([card for card in my_deck.cards if card.color == 'kier']) == 13
    assert len([card for card in my_deck.cards if card.color == 'karo']) == 13


def test_deck_figures():
    for figure in Card.card_figures:
        assert len([card for card in Deck().cards if card.figure == figure]) == 4


def test_shuffle():
    my_deck = Deck()
    cards = my_deck.cards[:]
    my_deck.shuffle()
    assert cards != my_deck.cards


def test_draw_one():
    my_deck = Deck()
    drawn_card = my_deck.draw()
    assert len(my_deck.cards) == 51
    assert drawn_card not in my_deck.cards
