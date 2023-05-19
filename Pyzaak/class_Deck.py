# This class will be the base class for the table deck and the side deck.
#   To do:
#   Create derivative classes for table deck and side deck.

class Deck:
    def __init__(self, numCards):
        self.size = numCards

    def shuffle(self):
        # To do:
        # implement a randomizer function.

    def draw(self, num):
        # To do:
        # implement a function to take the requested number of cards from the "top" of the deck.

    def peek(self):
        # To do:
        # implement a function to look at the top card and shuffle it back in.