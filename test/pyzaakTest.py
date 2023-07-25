# This file will serve as a unit tester for project files.

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Pyzaak')))
from class_Card import Card
from class_Deck import Deck
from class_Hand import Hand
import random

    # Setting up a file to record results:
orig_stdout = sys.stdout
results = open('testResults.txt', 'w')
sys.stdout = results

    # Testing
print("Testing Card class...")
testCard = Card(random.randint(1,10))
print("\tPositive, no flip:\n", testCard.debug())
testCard = Card(random.randint(-10, -1), True)
print("\tNegative, flip:\n", testCard.debug())
del testCard
print("\n")

print("Testing Deck class...")
mainDeck = Deck(True)
print("\tMain deck:\n", mainDeck.debug())
del mainDeck
sideDeck = Deck(False)
print("\t Side deck::\n", sideDeck.debug())
print("\n")

print("Testing Hand class...")
testHand = Hand(sideDeck.draw(4))
print(testHand.debug())
del testHand
del sideDeck
print("\n")

# TODO: test ComPlayer

# TODO: test Pyzaak class

    # Revert output:
results.close()
sys.stdout = orig_stdout