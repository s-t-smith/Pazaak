# This is the card class inherited from the base class.
# This class represents the cards used in the player's hand.

import class_Card

class HandCard(class_Card):
    def __init__(self, val, sign):
        super.__init__(val)
        self.sign = sign

    def flip(self):
        if(self.sign == "plus"):
            self.sign = "minus"
        else:
            self.sign = "plus"