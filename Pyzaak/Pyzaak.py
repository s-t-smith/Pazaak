# This file will be the overall main for the game.

from class_GameBoard import GameBoard
from class_Deck import Deck
from class_Card import Card
from class_Hand import Hand

class Pyzaak():
	
    def __init__(self):
        
        # Create the table deck:
        tableDeck = Deck(True)

        # Initialize scores:
        playerScore = 0
        cpuScore = 0

        # Create player decks:
        playerDeck = Deck(False)
        cpuDeck = Deck(False)

        # Create player hands:
        playerHand = Hand(playerDeck.draw(4))
        cpuHand = Hand(cpuDeck.draw(4))

        # Choose first player turn:
        playerTurnDraw = tableDeck.peek()
        cpuTurnDraw = tableDeck.peek()
        if playerTurnDraw > cpuTurnDraw:
            playerFirst = True
        else:
            playerFirst = False