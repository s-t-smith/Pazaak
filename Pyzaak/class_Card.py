# This class will be the base class for deck cards and hand cards.
# To do:
#   Create derivative classes;
#   Hand card should implement a flip() function to change sign (+/-).

class Card:
    def __init__(self, val):
        self.value = val