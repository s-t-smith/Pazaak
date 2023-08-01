# This class will implement the window to display the game during play.
### Started writing this for tkinter, but might try a different moddule.

import tkinter
from class_Pyzaak import Pyzaak

# Extends the Tk class:
class GameBoard(tkinter.Tk):
    def __init__(self):
        super().__init__()
            # super() apparently to expose methods from Tk to the GameBoard class, lets us use the base class __init__.
        
        # Set configuration options for the root window (self):
        self.title("Pyzaak")
            # I'll have to look up more configuration options that would be useful.
        baseFrame = tkinter.Frame(self)
        baseFrame.pack()

        # Create a dictionary of frames:
        self.gameFrames = {}
            ### Game start
            ### Game in play
            ### Game over
        for F in (GameStart, GamePlay, GameOver):
            frame = F(self, baseFrame)
            self.gameFrames[F] = frame
            frame.pack()

        # TODO: instantiate a game object?

        # End by raising the starting window:
        self.switchFrame(GameStart)
        
    def switchFrame(self, frame):
        target = self.gameFrames[frame]
        target.tkraise()
    
    def __main__(self):
        self.mainloop()

class GameStart(tkinter.Frame):
    def __init__(self, parent, container):
        super().__init__(self, parent)
        self.title("Start")
    ### Should contain:
        # Brief intro
        # Button: Start
        # Button: Quit

    ### Placeholder/debugger
        self.btn_Check = tkinter.Button(text="Next", command=container.switchFrame(GamePlay))
        self.btn_Check.pack()

class GamePlay(tkinter.Frame):
    def __init__(self, parent, container):
        super().__init__(self, parent)
        self.title("Play")
    ### Should contain:
        # Player's board
        # CPU's board
        # Button: Quit

    ### Placeholder/debugger
        self.btn_Check = tkinter.Button(text="Next", command=container.switchFrame(GameOver))
        self.btn_Check.pack()

class GameOver(tkinter.Frame):
    def __init__(self, parent, container):
        super.__init__(self, parent)
        self.title("Game Over")
    ### Should contain:
        # Summary of last game
        # Button: Play Again
        # Button: Quit

    ### Placeholder/debugger
        self.btn_Check = tkinter.Button(text="Next", command=container.switchFrame(GameStart))
        self.btn_Check.pack()

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
            ### this will need to be adjusted to read the variable from the game object.
            ### wrap in an if() for player/CPU and set textvariable=Pyzaak.<player>Score.
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