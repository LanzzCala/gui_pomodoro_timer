from tkinter import *
from tkinter import ttk

class Pomodoro:
    def __init__(self, root):

        root.title("Pomodoro Timer")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky= (N, W, E, S))
        mainframe.pack(padx=10, pady=65)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.minsize(400, 200)
        root.maxsize(400, 200)
        
        #Establish primary buttons
        ttk.Button(mainframe, text="Pomodoro").grid(column=1, row=1, sticky=(N, W))
        ttk.Button(mainframe, text="Short break").grid(column=2, row=1, sticky=(N))
        ttk.Button(mainframe, text="Long break").grid(column=3, row=1, sticky=(S, W))
        ttk.Button(mainframe, text="Start").grid(column=1, row=3, sticky=(S, E))
        ttk.Button(mainframe, text="Reset").grid(column=3, row=3, sticky=(S, W))
        
        
        


root = Tk()
Pomodoro(root)
root.mainloop()