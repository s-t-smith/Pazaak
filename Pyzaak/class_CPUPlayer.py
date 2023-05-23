# This class will handle the decision-making for the computer player (user's opponent).

from class_Hand import Hand

class CPUPlayer:
    def __init__(self) -> None:
        pass    # placeholder

    # TODO: create decision tree;
        # if the current score is close under 20, play the card that gets it closest to 20.
        # if the current score is over 20, play the card that gets it closest but under 20.
        # if the current score is close to 20 and no cards will get closer, "Stand" (return 99).
        # if the current score is not close to 20, "End Turn" (return 0).
        
    def playCard(hand: Hand, index: int) -> int:
        return hand.play(index)

    def shouldStand(cpuScore: int, hand: Hand) -> bool:
        if cpuScore == 20:
            # Stop when you hit:
            return True
        else:
            gap = 20 - cpuScore
            if gap > 0 and gap <= 4:
                # For scores just under 20, Stand:
                return True
            # TODO: expand for scores over 20.
            return False
    
    def shouldEndTurn(cpuScore: int, hand: Hand) -> bool:
        for card in hand.cards:
            if cpuScore + card.show() == 20:
                # Don't stop if you can hit:
                return False