# This class will be the base class for deck cards and hand cards.

class Card:
    def __init__(self, val: int, canFlip: bool=False):
        self.value = val
        self.canFlip = canFlip

    def show(self) -> int:
        return self.value

    def flip(self) -> None:
        if self.canFlip:
            self.value *= -1

    # Going to use this for some manual testing:
    def debug(self) -> str:
        # print("Value: ", self.value, '\n', "Flip: ", self.canFlip, '\n')
        outstr = "Value: "+str(self.value)+'\n'+"Flip: "+str(self.canFlip)+'\n'
        return outstr