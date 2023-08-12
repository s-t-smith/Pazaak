# This file will serve as a unit tester for project files.

import sys, os
import random
# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Pyzaak')))
### export PYTHONPATH=pwd
from Pyzaak.class_Card import Card
from Pyzaak.class_Deck import Deck
from Pyzaak.class_Hand import Hand
from Pyzaak.class_Pyzaak import Pyzaak

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

# TODO: test Pyzaak class
print("Testing Pyzaak class...")
testGame = Pyzaak()
# print(os.getcwd())
print(testGame)
testGame._graph().write_png(os.getcwd())

# TODO: test ComPlayer

    # Revert output:
results.close()
sys.stdout = orig_stdout