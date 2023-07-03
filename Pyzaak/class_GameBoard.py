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

        # Create Start frame:
           # Keeps the app from launching straight into a game.
            ### The base Frame for the starting window:
        self.startFrame = tkinter.Frame(self)
        self.startFrame.title = tkinter.Label(self.startFrame, text="Pyzaak")
        self.startFrame.title.grid(row=0, column=0, sticky='N')
            ### A brief guide for any new players (or reminder for returning users):
            # TODO: get this working...
        guideText = open(os.getcwd()+'\\guide.txt').read()
        self.startFrame.guide = tkinter.Label(self.startFrame, textvariable=guideText)
        self.startFrame.guide.grid(row=1, column=0)
            
            ### The starting window will only have two options; "Play" to start a game, or "Quit" to exit the app:
        self.btn_Start = tkinter.Button(self.startFrame, text="Play", command=self.gameStart)
        self.btn_Start.grid(row=2, column=0)
        self.btn_startQuit = tkinter.Button(self.startFrame, text="Quit", command=self.destroy)
        self.btn_startQuit.grid(row=3, column=0)
        
        # Bring the starting window to the front of the app:
        self.startFrame.pack()
        self.startFrame.tkraise()
        
    def gameStart(self):
        
        self.gameFrame = tkinter.Frame(self)
        self.gameFrame.title = tkinter.Label(self.gameFrame, text="Pyzaak")
        self.gameFrame.title.grid(row=0, column=1, sticky='N')

        # Create player's side of the table:
        self.playerSide = BoardSide(self.gameFrame, playerName="Player")
        self.playerSide.grid(row=1, column=0)

        # Create CPU's side of the table:
        self.cpuSide = BoardSide(self.gameFrame, playerName="CPU")
        self.cpuSide.grid(row=1, column=2)

        self.btn_gameQuit = tkinter.Button(self.gameFrame, text="Quit", command=self.__init__())
        self.btn_gameQuit.grid(row=2, column=1)

        # Swap the opening frame for the game frame.
        self.gameFrame.pack()
        self.gameFrame.tkraise()
    
    def gameOver(self):
        # Announce the end of the game and declare the winner:
        self.GOFrame = tkinter.Frame(self)
        self.GOFrame.title = tkinter.Label(self.GOFrame, text="Game Over")
        self.GOFrame.title.grid(row=0, column=0, sticky='N')
        
        # Buttons:
        self.GOFrame.btn_Again = tkinter.Button(self.GOFrame, text="Play again", command=self.gameStart)
        self.GOFrame.btn_Again.grid(row=2, column=0)
        self.GOFrame.btn_Quit = tkinter.Button(self.GOFrame, text="Quit", command=self.destroy)
        self.GOFrame.btn_Quit.grid(row=2, column=1)
        
        self.GOFrame.pack()
        self.GOFrame.tkraise()

    def __main__(self):
        self.mainloop()

class BoardSide(tkinter.Frame, playerName):
    def __init__(self):
        super().__init__()
        # TODO: Create player frame:
        # Player frame will include;
        self.title = tkinter.Label(self, text=playerName)
            # Round counters
            # Score
        self.scoreBanner = tkinter.PanedWindow(self)
        self.playerRoundCounterA = tkinter.Checkbutton(self.scoreBanner, state="disabled")
        self.playerRoundCounterA.pack(side="left")
        self.playerRoundCounterB = tkinter.Checkbutton(self.scoreBanner, state="disabled")
        self.playerRoundCounterB.pack(side="left")
        self.playerRoundCounterC = tkinter.Checkbutton(self.scoreBanner, state="disabled")
        self.playerRoundCounterC.pack(side="left")
        self.playerCurrentScore = tkinter.Label(self.scoreBanner, text="0")
        self.playerCurrentScore.pack(side="right", padx=10)
        self.scoreBanner.grid(row=0, column=0)
            # Card grid (play area)
            # Hand grid (buttons)
            # End Turn button
            # Stand button
        