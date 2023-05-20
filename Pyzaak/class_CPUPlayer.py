# This class will handle the decision-making for the computer player (user's opponent).

from class_Hand import Hand

class CPUPlayer:
    def __init__(self) -> None:
        pass    # placeholder
        
    def pickCard(cpuScore: int, hand: Hand) -> int:
        pass    # placeholder
        # TODO: create decision tree;
            # if the current score is close under 20, play the card that gets it closest to 20.
            # if the current score is over 20, play the card that gets it closest but under 20.
            # if the current score is close to 20 and no cards will get closer, "Stand" (return 99).
            # if the current score is not close to 20, "End Turn" (return 0).