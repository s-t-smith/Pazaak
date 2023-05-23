# This class will handle the decision-making for the computer player (user's opponent).

from class_Hand import Hand

class CPUPlayer:
    def __init__(self) -> None:
        pass    # placeholder

    # TODO: create decision tree;
        # Compare score to target.
        # If playing a card gets to 20, play and Stand.
        # If playing a card does not get to 20, make another decision:
            # If score is well under 20, End Turn.
            # If score is less but close to 20, Stand.
        
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