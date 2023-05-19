# This is the deck class inherited from the base class.
# This class represents the cards used to make hands during a game.

import class_Deck

class SideDeck(class_Deck):
    def __init__(self):
        super.__init__(10)