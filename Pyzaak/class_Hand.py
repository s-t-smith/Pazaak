# This is the class to implement the player's hand of cards for a game.

from class_Card import Card

class Hand:
    def __init__(self, drawCards: list):
        self.cards = drawCards

    def play(self, card: int) -> int:
        playedVal = self.cards[card].show()
        self.cards.remove(self.cards[card])
        return playedVal
    
    def add(self, card: Card) -> None:
        if len(self.cards) < 4:
            self.cards.append(card)
    
    # Going to use this for some manual testing:
    def __str__(self) -> str:
        outString = ""
        for card in self.cards:
            # outString += f"{card.show()}, "
            outString = f"{outString} {card.show()},"
        return outString
