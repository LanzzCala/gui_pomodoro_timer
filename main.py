from tkinter import *
from tkinter import ttk
import time

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
        ttk.Button(mainframe, text="Pomodoro", command=self.pomodoro_start).grid(column=1, row=1, sticky=(N, W))
        ttk.Button(mainframe, text="Short break").grid(column=2, row=1, sticky=(N))
        ttk.Button(mainframe, text="Long break").grid(column=3, row=1, sticky=(S, W))
        ttk.Button(mainframe, text="Start").grid(column=1, row=3, sticky=(S, E))
        ttk.Button(mainframe, text="Reset").grid(column=3, row=3, sticky=(S, W))

        #Declaration of variables
        minute = StringVar()
        second = StringVar()

        #Set default value of numbers to 0
        minute.set("00")
        second.set("00")

        minute_entry = ttk.Entry(mainframe, width=6, font=(15), textvariable=minute)
        minute_entry.grid(column=1, row=2,sticky=(E))
        second_entry = ttk.Entry(mainframe, width=6, font=(15), textvariable=second)
        second_entry.grid(column=3, row=2, sticky=(W))
        
    def pomodoro_start(self):
        print("Time to start!")
    
        
        


root = Tk()
Pomodoro(root)
root.mainloop()