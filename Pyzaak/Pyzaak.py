# This file will be the overall main for the game.

import class_GameBoard
import class_Deck
import class_Card

class Pyzaak():
	
    def __init__(self):
        # Create the table deck:
        tableDeck = class_Deck(True)

        # Create player decks:
        playerDeck = class_Deck(False)
        cpuDeck = class_Deck(False)

        # TODO: create player hands
        # TODO: choose first turn