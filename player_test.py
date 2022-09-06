from player import Player
from deck import Deck
from card import Card


def test_get_cards():
    """Get two cards"""
    player = Player('Gracz')
    my_deck = Deck()
    my_deck.shuffle()
    player.get_cards(my_deck.draw())
    player.get_cards(my_deck.draw())
    assert len(player.hand.cards) == 2


def test_calc_points():
    """['A', '3']"""
    player = Player('Gracz')
    player.get_cards(Card('A', 'pik'))
    player.get_cards(Card(3, 'pik'))
    assert player.hand.value == 14


def test_calc_two_aces():
    """['A', 'A']"""
    player = Player('Gracz')
    player.get_cards(Card('A', 'pik'))
    player.get_cards(Card('A', 'karo'))
    assert player.hand.value == 12


def test_calc_three_aces():
    """['A', 'A', 'A']"""
    player = Player('Gracz')
    player.get_cards(Card('A', 'pik'))
    player.get_cards(Card('A', 'karo'))
    player.get_cards(Card('A', 'trefl'))
    assert player.hand.value == 13
