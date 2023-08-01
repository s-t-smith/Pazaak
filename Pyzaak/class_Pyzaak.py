# This file will implement the game state for a session of Pazaak.

from class_Deck import Deck
from statemachine import StateMachine, State

class Pyzaak(StateMachine):
	
    # States:
    GameInit = State(initial=True)
    UserTurn = State()
    ComTurn = State()
    RoundOver = State()
    GameOver = State()

    # Actions:
    gameStart = (
        GameInit.to(UserTurn)
        | GameInit.to(ComTurn)
    )
    turnCont = (
        UserTurn.to(ComTurn)
        | ComTurn.to(UserTurn)
    )
    roundEnd = (
        UserTurn.to(RoundOver)
        | ComTurn.to(RoundOver)
    )
    gameEnd = (
        RoundOver.to(GameOver)
    )
    gameCont = (
        RoundOver.to(UserTurn)
        | RoundOver.to(ComTurn)
    )

    # Fields:
    ### userScore
    ### comScore
    ### userRounds
    ### comRounds

    # Class methods:
    