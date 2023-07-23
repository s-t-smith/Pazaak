# This file will be the overall main for the game.

from class_Deck import Deck
from statemachine import StateMachine, State

class Pyzaak(StateMachine):
	UserTurn = State()
    ComTurn = State()
    GameOver = State()

    cycle = ()

    def __init__(self):
        super.__init__()

        # Initialize scores:
            # these are for tracking a round's score:
        self.userScore = 0
        self.comScore = 0
            # these are for tracking the number of rounds won:
        self.userRounds = 0
        self.comRounds = 0

        if pickFirstTurn(tableDeck=tableDeck):
            UserTurn.to.itself()
        else:
            ComTurn.to.itself()

    # TODO: figure out how this game object will interact with the game board.
        ### probably need a lot of pass-by-ref.
    # TODO: add more methods for implimenting the game rules.
        ### Maybe create a state machine?

    def addUserScore(self, score: int) -> None:
        self.userScore += score

    def reportUserScore(self) -> int:
        return self.userScore

    def userRoundWin(self) -> None:
        self.userRounds += 1

    def reportUserRounds(self) -> int:
        return self.userRounds
    
    def addComScore(self, score: int) -> None:
        self.comScore += score

    def reportComScore(self) -> int:
        return self.comScore

    def comRoundWin(self) -> None:
        self.comRounds += 1

    def reportComRounds(self) -> int:
        return self.comRounds

    def pickFirstTurn(tableDeck: Deck) -> bool:
    # Choose first player turn:
        userTurnDraw = tableDeck.peek()
        comTurnDraw = tableDeck.peek()
        if userTurnDraw >= comTurnDraw:
            return True
        else:
            return False