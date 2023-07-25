# This file will be the overall main for the game.

from class_Deck import Deck
from statemachine import StateMachine, State

class Pyzaak(StateMachine):
	UserTurn = State()
    ComTurn = State()
    RoundOver = State()
    GameOver = State()

    turnStep = (
        UserTurn.to(ComTurn)
        | ComTurn.to(UserTurn)
    )

    def __init__(self, deck: Deck):
        super.__init__()

        # Initialize scores:
            # these are for tracking a round's score:
        self.userScore = 0
        self.comScore = 0
            # these are for tracking the number of rounds won:
        self.userRounds = 0
        self.comRounds = 0

        if pickFirstTurn(deck):
            self.UserTurn.to.itself()
        else:
            self.ComTurn.to.itself()

    # TODO: figure out how this game object will interact with the game board.
        ### Maybe implement the entire game in the Pyzaak class and pass data to the board only for display.
    # TODO: add more methods for implimenting the game rules.
        ### This will be necessary if the game board does less; it will likely just be used to show card values on screen.

    def addUserScore(self, score: int) -> None:
        self.userScore += score
        if self.userScore >= 21:
            # go to round over
            pass    # placeholder

    def reportUserScore(self) -> int:
        return self.userScore

    def userRoundWin(self) -> None:
        self.userRounds += 1
        if self.userRounds == 3:
            # go to game over
            pass    # placeholder

    def reportUserRounds(self) -> int:
        return self.userRounds
    
    def addComScore(self, score: int) -> None:
        self.comScore += score
        if self.comScore >= 21:
            # go to round over
            pass    # placeholder

    def reportComScore(self) -> int:
        return self.comScore

    def comRoundWin(self) -> None:
        self.comRounds += 1
        if self.comRounds == 3:
            # got to game over
            pass    # placeholder

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