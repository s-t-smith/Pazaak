# This class will implement the window to display the game during play.

import tkinter

# Extends the Tk class:
class GameBoard(tkinter.Tk):
    def __init__(self):
        super().__init__()
            # super() apparently to expose methods from Tk to the GameBoard class, lets us use the base class __init__.
        
        # Set configuration options for the root window:
        self.title("Pyzaak")

        # TODO: Create frames:
        # Should have a start page with "Start" and "Quit"
        # Next should be the actual game page.
        self.startFrame = tkinter.Frame(self)
        self.gameFrame = tkinter.Frame(self)
        
        # TODO: Create basic buttons.
        self.btn_Start = tkinter.Button(self.startFrame, text="Start", command=self.gameFrame.tkraise())
        self.btn_Start.pack()
        self.btn_Quit = tkinter.Button(self.startFrame, text="Quit", command=self.quit())
        self.btn_Quit.pack()
        self.startFrame.pack()
        self.gameFrame.pack()
        self.startFrame.tkraise()
        
        
    def __main__(self):
        self.mainloop()
