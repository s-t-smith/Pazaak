# This file will be the overall main for the game.

from class_Deck import Deck
# from class_Card import Card
    # Already imported by Deck
from class_Hand import Hand
from class_CPUPlayer import CPUPlayer

class Pyzaak():
	
    def __init__(self):
        
        # Create CPU Player:
        self.CPU = CPUPlayer()

        # Create the table deck:
        self.tableDeck = Deck(True)

        # Initialize scores:
            # these are for tracking a round's score:
        self.playerScore = 0
        self.cpuScore = 0
                    # these are for tracking the number of rounds won:
        self.playerRounds = 0
        self.cpuRounds = 0

        # Create player decks:
        self.playerDeck = Deck(False)
        self.cpuDeck = Deck(False)

        # Create player hands:
        self.playerHand = Hand(self.playerDeck.draw(4))
        self.cpuHand = Hand(self.cpuDeck.draw(4))

        # Choose first player turn:
        playerTurnDraw = self.tableDeck.peek()
        cpuTurnDraw = self.tableDeck.peek()
        if playerTurnDraw >= cpuTurnDraw:
            self.playerFirst = True
        else:
            self.playerFirst = False

    # TODO: figure out how this game object will interact with the game board.
    
    # Using this for some manual testing, probably not useful for runtime:
    def __str__(self) -> str:
        outString = f"Player Score: {self.playerScore}\n"
        outString += f"Player Hand: "
        for card in self.playerHand.cards:
            outString = f"{outString} {card.show()}"
        outString += "\n\n"
        outString += f"Computer Score: {self.cpuScore}\n"
        outString += f"Computer Hand: "
        for card in self.cpuHand.cards:
            outString = f"{outString} {card.show()}"
        return outString