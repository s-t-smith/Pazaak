# This file will implement the game state for a session of Pazaak.

from Pyzaak.class_Deck import Deck
from statemachine import StateMachine, State

class Pyzaak(StateMachine):
	
    # States:
    GameInit = State(name='Game Start', initial=True)
    UserTurn = State(name='Player Turn')
    ComTurn = State(name='Computer Turn')
    RoundOver = State(name='End of Round')
    GameOver = State(name='Game Over', final=True)

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
    def on_enter_UserTurn(self):
        pass    # placeholder

    def on_exit_UserTurn(self):
        pass    # placeholder

    def on_enter_ComTurn(self):
        pass    # placeholder

    def on_exit_ComTurn(self):
        pass    # placeholder

    def on_enter_RoundOver(self):
        pass     # placeholder