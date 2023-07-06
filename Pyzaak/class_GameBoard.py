# This class will implement the window to display the game during play.

import tkinter
import os
from typing import Any
from class_Pyzaak import Pyzaak

# Extends the Tk class:
class GameBoard(tkinter.Tk):
    def __init__(self):
        super().__init__()
            # super() apparently to expose methods from Tk to the GameBoard class, lets us use the base class __init__.
        
        # Set configuration options for the root window (self):
        self.title("Pyzaak")
            # I'll have to look up more configuration options that would be useful.

        # TODO: Create a dictionary of frames:
            ### Game start
            ### Game in play
            ### Game over
        
    
    def __main__(self):
        self.mainloop()

class BoardSide(tkinter.Frame):
    def __init__(self, playerName):
        super().__init__()
        # Player frame will include;
        self.title = tkinter.Label(self, text=playerName)
            # Round counters
            # Score
        self.scoreBanner = tkinter.PanedWindow(self)
        self.roundCounterA = tkinter.Checkbutton(self.scoreBanner, state="disabled")
        self.roundCounterA.grid(row=0, column=0)
        self.roundCounterB = tkinter.Checkbutton(self.scoreBanner, state="disabled")
        self.roundCounterB.grid(row=0, column=1)
        self.roundCounterC = tkinter.Checkbutton(self.scoreBanner, state="disabled")
        self.roundCounterC.grid(row=0, column=2)
        self.currentScore = tkinter.Label(self.scoreBanner, text="0")
        self.currentScore.grid(row=0, column=3)
        self.scoreBanner.grid(row=0, column=0)
            # Card grid (play area)
        self.cardGrid = tkinter.PanedWindow(self)
        
        self.cardGrid.grid(row=1, column=0)
            # Hand grid (buttons)
        self.handGrid = tkinter.PanedWindow(self)

        self.handGrid.grid(row=2, column=0)

        ### If the frame is for the human player:
            # End Turn button
            # Stand button
        if playerName!="CPU":
            self.buttonGrid = tkinter.PanedWindow(self)
            self.buttonGrid.btn_ET = tkinter.Button(self.buttonGrid, text="End Turn")
            self.buttonGrid.btn_ET.grid(row=0, column=0)
            self.buttonGrid.btn_ST = tkinter.Button(self.buttonGrid, text="Stand")
            self.buttonGrid.btn_ST.grid(row=0, column=1)
            self.buttonGrid.grid(row=3, column=0)

class GameStart(tkinter.Frame):
    pass #placeholder

class GamePlay(tkinter.Frame):
    pass #placeholder

class GameOver(tkinter.Frame):
    pass #placeholder