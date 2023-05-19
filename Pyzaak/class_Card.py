# This class will be the base class for deck cards and hand cards.
# To do:
#   Create derivative classes;
#   Hand card should implement a flip() function to change sign (+/-).

class Card:
    def __init__(self, val: int, canFlip: bool=False):
        self.value = val
        self.canFlip = canFlip

    def show(self) -> int:
        return self.value

    def flip(self) -> None:
        if self.canFlip:
            self.value *= -1