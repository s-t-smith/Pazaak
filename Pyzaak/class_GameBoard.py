# This class will implement the window to display the game during play.

import tkinter
import os
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
        self.guideText = open(os.getcwd()+'\\guide.txt').read()
        self.startFrame.guide = tkinter.Label(self.startFrame, textvariable=self.guideText)
        self.startFrame.guide.grid(row=1, column=0)
            
            ### The starting window will only have two options; "Play" to start a game, or "Quit" to exit the app:
        self.btn_Start = tkinter.Button(self.startFrame, text="Play", command=self.gameStart)
        self.btn_Start.grid(row=2, column=0)
        self.btn_startQuit = tkinter.Button(self.startFrame, text="Quit", command=self.destroy)
        self.btn_startQuit.grid(row=3, column=0)
        self.startFrame.pack()
            ### Bring the starting window to the front of the app:
        
        self.startFrame.tkraise()
        
    def gameStart(self):

        ### Instantiate a game:
        self.game = Pyzaak()

        # TODO: Create Game frame:
            # Where the actual game will happen.
            ### The base Frame for the main game window:
        self.gameFrame = tkinter.Frame(self)
        self.gameFrame.title = tkinter.Label(self.gameFrame, text="Pyzaak")
        
        # TODO: Create player frame:
        ### Player frame will include;
        self.playerFrame = tkinter.Frame(self.gameFrame)
        self.playerFrame.title = tkinter.Label(self.playerFrame, text="Player")
            # Round counters
            # Score
        self.scoreBanner = tkinter.PanedWindow(self.playerFrame)
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
            # Quit button
        self.playerFrame.pack()
        

        # TODO: Create CPU frame:
        ### CPU frame will include;
            # Round counters
            # Score
            # Card grid (play area)
            # Hand grid (hidden cards)

        ### Closes the starting window and brings up the main game window:
        self.startFrame.destroy()
        self.gameFrame.pack()
        self.gameFrame.tkraise()
    
    def gameOver(self):
        # Announce the end of the game and declare the winner:
        self.GOFrame = tkinter.Frame(self)
        self.GOFrame.title = tkinter.Label(self.GOFrame, text="Game Over")
        self.GOFrame.title.grid(row=0, column=0, sticky='N')
        if self.game.playerRounds > self.game.cpuRounds:
            self.GOFrame.winner = tkinter.Label(self.GOFrame, text="Player wins!")
            self.GOFrame.winner.grid(row=1, column=0)
        elif self.game.cpuRounds > self.game.playerRounds:
            self.GOFrame.winner = tkinter.Label(self.GOFrame, text="Python wins!")
            self.GOFrame.winner.grid(row=1, column=0)

        # Buttons:
        self.GOFrame.btn_Again = tkinter.Button(self.GOFrame, text="Play again", command=self.gameStart)
        self.GOFrame.btn_Again.grid(row=2, column=0)
        self.GOFrame.btn_Quit = tkinter.Button(self.GOFrame, text="Quit", command=self.destroy)
        self.GOFrame.btn_Quit.grid(row=2, column=1)
        
        self.GOFrame.pack()
        self.GOFrame.tkraise()

    def __main__(self):
        self.mainloop()
