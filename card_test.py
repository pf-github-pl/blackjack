import pytest

from card import Card
from card import InvalidCardFigure, InvalidCardColor


def test_card_creation():
    card = Card('A', 'pik')
    assert card.figure == 'A'
    assert card.color == 'pik'


def test_card_creation_wrong_figure():
    with pytest.raises(InvalidCardFigure) as message:
        Card('Asik', 'pik')
        assert message == 'Invalid card figure'


def test_card_creation_wrong_color():
    with pytest.raises(InvalidCardColor) as message:
        Card('A', 'piczek')
        assert message == 'Invalid card color'


def test_card_representation():
    assert repr(Card('A', 'pik')) == 'A pik'
