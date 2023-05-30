# This class will implement the window to display the game during play.

import tkinter
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
        self.startFrame.title.pack()
            ### A brief guide for any new players (or reminder for returning users):
            # TODO: get this working...
        guideText = open('guide.txt').read()
        self.startFrame.guide = tkinter.Label(self.startFrame, textvariable=guideText)
        self.startFrame.guide.pack()
            ### The starting window will only have two options; "Play" to start a game, or "Quit" to exit the app:
        self.btn_Start = tkinter.Button(self.startFrame, text="Play", command=self.gameStart)
        self.btn_Start.pack()
        self.btn_startQuit = tkinter.Button(self.startFrame, text="Quit", command=self.destroy)
        self.btn_startQuit.pack()
        self.startFrame.pack()
            ### Bring the starting window to the front of the app:
        self.startFrame.tkraise()
        
    def gameStart(self):
        ### Closes the starting window and brings up the main game window:
        self.startFrame.destroy()

        # TODO: Create Game frame:
            # Where the actual game will happen.
            ### The base Frame for the main game window:
        self.gameFrame = tkinter.Frame(self)
        self.gameFrame.title = tkinter.Label(self.gameFrame, text="Pyzaak")
        self.gameFrame.title.pack()
            ### The user will have several buttons for turn actions;
            # TODO: create buttons for the hand cards.
                ### - End Turn: Pass to the next player.
        self.btn_EndTurn = tkinter.Button(self.gameFrame, text="End Turn")
        self.btn_EndTurn.pack()
                ### - Stand: Keep the current score for the rest of the round.
        self.btn_Stand = tkinter.Button(self.gameFrame, text="Stand")
        self.btn_Stand.pack()
                ### - Quit: Exit the app.
        self.btn_gameQuit = tkinter.Button(self.gameFrame, text="Quit", command=self.destroy)
        self.btn_gameQuit.pack(side = "bottom")

        ### Place and bring the game window to the front:
        self.gameFrame.pack()
        self.gameFrame.tkraise()

        ### Instantiate a game:
        self.game = Pyzaak()
    
    def gameOver(self):
        # TODO: make a "game over" window to restart or quit.
        pass    # placeholder

    def __main__(self):
        self.mainloop()
