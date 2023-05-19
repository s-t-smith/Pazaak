# This class will be the base class for the table deck and the side deck.

import class_Card
import random

class Deck:
    def __init__(self, isMainDeck: bool):
        self.cards = []
        if isMainDeck:
            for val in range(10):
                for card in range(4):
                    self.cards.append(class_Card(val+1))
        else:
            cardChoices = [val for val in range(-6, 7) if val != 0]
            random.shuffle(cardChoices)
            self.cards = [class_Card(val, random.choices([True, False], [1, 3])) for val in cardChoices[:10]]


    def shuffle(self) -> None:
        self.cards.shuffle()

    def draw(self, num: int) -> list:
        cardsDrawn = self.cards[0:num]
        del self.cards[0:num]
        return cardsDrawn

    def peek(self) -> int:
        cardValue = self.cards[0].show()
        self.shuffle()
        return cardValue