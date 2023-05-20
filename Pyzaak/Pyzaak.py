# This file will be the overall main for the game.

from class_GameBoard import GameBoard
from class_Deck import Deck
from class_Card import Card

class Pyzaak():
	
    def __init__(self):
        # Create the table deck:
        tableDeck = Deck(True)

        # Create player decks:
        playerDeck = Deck(False)
        cpuDeck = Deck(False)

        # TODO: create player hands
        # TODO: choose first turn