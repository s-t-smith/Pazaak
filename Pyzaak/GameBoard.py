import tkinter

# Extends the Tk class:
class GameBoard(tkinter.Tk):
    def __init__(self):
        super().__init__() # super() apparently to expose methods from Tk to the GameBoard class, lets us use the base class __init__.
        
        # Set configuration options for the root window:
        self.title("Pyzaak")
        
        # Set buttons:
        self.buttonEndTurn
        self.buttonStand
        self.buttonQuit