# This class will implement the window to display the game during play.

import tkinter

# Extends the Tk class:
class GameBoard(tkinter.Tk):
    def __init__(self):
        super().__init__()
            # super() apparently to expose methods from Tk to the GameBoard class, lets us use the base class __init__.
        
        # Set configuration options for the root window (self):
        self.title("Pyzaak")

        # Create Start frame:
        self.startFrame = tkinter.Frame(self)   # Keeps the app from launching straight into a game.
        self.startFrame.title = tkinter.Label(self.startFrame, text="Pyzaak")
        self.startFrame.title.pack()
        self.btn_Start = tkinter.Button(self.startFrame, text="Play", command=self.gameStart)
        self.btn_Start.pack()
        self.btn_startQuit = tkinter.Button(self.startFrame, text="Quit", command=self.destroy)
        self.btn_startQuit.pack()
        self.startFrame.pack()
        self.startFrame.tkraise()
        
        # TODO: Create Game frame:
        self.gameFrame = tkinter.Frame(self)    # Where the actual game will happen.
        self.gameFrame.title = tkinter.Label(self.gameFrame, text="Pyzaak")
        self.gameFrame.title.pack()
        self.btn_gameQuit = tkinter.Button(self.gameFrame, text="Quit", command=self.destroy)
        self.btn_gameQuit.pack()
        
    def gameStart(self):
        self.startFrame.destroy()
        self.gameFrame.pack()
        self.gameFrame.tkraise()
    
    def __main__(self):
        self.mainloop()
