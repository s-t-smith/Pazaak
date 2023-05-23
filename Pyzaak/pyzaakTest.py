# This file will serve as a unit tester for project files.

from class_Card import Card
from class_Deck import Deck
from class_Hand import Hand
from Pyzaak import Pyzaak
import sys
import random

    # Setting up a file to record results:
orig_stdout = sys.stdout
results = open('testResults.txt', 'w')
sys.stdout = results

    # Testing
print("Testing Card class...")
testCard = Card(random.randint(1,10))
print(testCard)
testCard = Card(random.randint(-10, -1), True)
print(testCard)
del testCard
print("\n")

print("Testing Deck class...")
mainDeck = Deck(True)
print(mainDeck)
sideDeck = Deck(False)
print(sideDeck)
# del testDeck
print("\n")

print("Testing Hand class...")
testHand = Hand(sideDeck.draw(4))
print(testHand)
del testHand
del mainDeck
del sideDeck
print("\n")

print("Testing Pyzaak...")
print("Game initialize:")
testGame = Pyzaak()
print(testGame)

    # Revert output:
results.close()
sys.stdout = orig_stdout