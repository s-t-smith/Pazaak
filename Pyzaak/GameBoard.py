import tkinter

# Extends the Tk class:
class GameBoard(tkinter.Tk):
    def __init__(self):
        # super().__init__()
            # super() apparently to expose methods from Tk to the GameBoard class, lets us use the base class __init__.
            
        tkinter.Tk.__init__()
        
        # Set configuration options for the root window:
        self.title("Pyzaak")
        
        # Set buttons:
        self.buttonEndTurn = tkinter.Button(text="End Turn")
        self.buttonEndTurn.pack()
        self.buttonStand = tkinter.Button(text="Stand")
        self.buttonStand.pack()
        self.buttonQuit = tkinter.Button(text="Quit")
        self.buttonQuit.pack()
        
    def __main__(self):
        self.mainloop()