# This class will be the base class for the table deck and the side deck.

from class_Card import Card
import random

class Deck:
    def __init__(self, isMainDeck: bool):
        self.cards = []
        if isMainDeck:
            for val in range(10):
                for card in range(4):
                    self.cards.append(Card(val+1))
            # self.shuffle()
        else:
            cardChoices = [val for val in range(-6, 7) if val != 0]
            random.shuffle(cardChoices)
            self.cards = [Card(val, random.choices([True, False], [1, 3])) for val in cardChoices[:10]]


    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self, num: int) -> list:
        if self.cards.len() > num:
            cardsDrawn = self.cards[0:num]
            del self.cards[:num]
            return cardsDrawn

    def peek(self) -> int:
        cardValue = self.cards[0].show()
        self.shuffle()
        return cardValue

    # Going to use this for some manual testing:
    def __str__(self) -> str:
        outString = ""
        for card in self.cards:
            # outString += f"{card.show()}, "
            outString = f"{outString} {card.show()},"
        return outString