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
        ### Closes the starting window and brings up the main game window:
        self.startFrame.destroy()
        
        ### Instantiate a game:
        self.game = Pyzaak()

        # TODO: Create Game frame:
            # Where the actual game will happen.
            ### The base Frame for the main game window:
        self.gameFrame = tkinter.Frame(self)
        self.gameFrame.title = tkinter.Label(self.gameFrame, text="Pyzaak")
        self.gameFrame.title.grid(row=0, column=0)
        # TODO: create score and round markers:
        self.playerRounds = tkinter.Label(self.gameFrame, text= "() () ()")
        self.playerRounds.grid(row=0, column= 0, sticky= 'W')
        self.playerScore = tkinter.Label(self.gameFrame, textvariable=self.game.playerScore)
        self.playerScore.grid(row=0, column=1, sticky= 'E')
        # TODO: create area for deck cards:

            ### The user will have several buttons for turn actions;
        # TODO: create buttons for the hand cards.
                ### - End Turn: Pass to the next player.
        self.btn_EndTurn = tkinter.Button(self.gameFrame, text="End Turn")
        self.btn_EndTurn.grid(row=1, column=0)
                ### - Stand: Keep the current score for the rest of the round.
        self.btn_Stand = tkinter.Button(self.gameFrame, text="Stand")
        self.btn_Stand.grid(row=1, column=2)
                ### - Quit: Exit the app.
        self.btn_gameQuit = tkinter.Button(self.gameFrame, text="Quit", command=self.destroy)
        self.btn_gameQuit.grid(row=2, column=1)

        ### Place and bring the game window to the front:
        self.gameFrame.pack()
        self.gameFrame.tkraise()
    
    def gameOver(self):
        # TODO: make a "game over" window to restart or quit.
        pass    # placeholder

    def __main__(self):
        self.mainloop()
