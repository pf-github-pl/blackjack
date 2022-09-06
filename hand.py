class HandOverflow(Exception):
    def __str__(self):
        return '<<< PRZEKROCZONO 21. GRA SKOŃCZONA! >>>'


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
