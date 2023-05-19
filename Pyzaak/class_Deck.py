# This class will be the base class for the table deck and the side deck.
#   To do:
#   Create derivative classes for table deck and side deck.

class Deck:
    def __init__(self, numCards):
        self.size = numCards