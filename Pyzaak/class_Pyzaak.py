# This file will be the overall main for the game.

from class_Deck import Deck

class Pyzaak():
	
    def __init__(self):

        # Initialize scores:
            # these are for tracking a round's score:
        self.playerScore = 0
        self.cpuScore = 0
                    # these are for tracking the number of rounds won:
        self.playerRounds = 0
        self.cpuRounds = 0

    # TODO: figure out how this game object will interact with the game board.
        ### probably need a lot of pass-by-ref.
    # TODO: add more methods for implimenting the game rules.
        ### Maybe create a state machine?

    def addPlayerScore(self, score: int) -> None:
        self.playerScore += score

    def playerRoundWin(self) -> None:
        self.playerRounds += 1
    
    def addCPUScore(self, score: int) -> None:
        self.cpuScore += score

    def cpuRoudnWin(self) -> None:
        self.cpuRounds += 1

    def pickFirstTurn(tableDeck: Deck) -> bool:
    # Choose first player turn:
        playerTurnDraw = tableDeck.peek()
        cpuTurnDraw = tableDeck.peek()
        if playerTurnDraw >= cpuTurnDraw:
            return True
        else:
            return False