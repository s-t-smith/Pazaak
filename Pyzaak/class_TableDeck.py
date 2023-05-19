# This is the deck class inherited from the base class.
# This class represents the cards drawn during a game.

import class_Deck

class TableDeck(class_Deck):
    def __init__(self):
        super.__init__(40)
        # To do:
        # initialize a 40-card deck with cards valued 1..10 (four sets).