"""BlackJack Game - single card class"""


class InvalidCardFigure(Exception):
    """Exception when card figure is invalid"""


class InvalidCardColor(Exception):
    """"Exception when card color is invalid"""


class Card:
    """Card abstraction"""
    card_colors = ['kier', 'trefl', 'pik', 'karo']
    card_figures = list(range(2, 11)) + ['A', 'K', 'Q', 'J']

    def __init__(self, figure, color):
        if figure not in self.card_figures:
            raise InvalidCardFigure('Invalid card figure')
        self.figure = figure
        if color not in self.card_colors:
            raise InvalidCardColor('Invalid card color')
        self.color = color
        self.value = self.assign_value(figure)

    @staticmethod
    def assign_value(figure):
        """Assign card value on card figure"""
        if figure == 'A':
            return 11
        if figure in ['K', 'J', 'Q']:
            return 10
        if figure in list(range(2, 11)):
            return int(figure)
        raise ValueError

    def __str__(self):
        return f'{self.figure} {self.color}'

    def __repr__(self):
        return f'{self.figure} {self.color}'
