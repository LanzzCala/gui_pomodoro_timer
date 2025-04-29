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
        hour = StringVar()
        minute = StringVar()
        second = StringVar()

        #Set default value of numbers to 0
        hour.set("00")
        minute.set("00")
        second.set("00")
        hour_entry = ttk.Entry(mainframe, width=6, font=(15), textvariable=minute)
        hour_entry.grid(column=1, row=2)
        minute_entry = ttk.Entry(mainframe, width=6, font=(15), textvariable=minute)
        minute_entry.grid(column=2, row=2)
        second_entry = ttk.Entry(mainframe, width=6, font=(15), textvariable=second)
        second_entry.grid(column=3, row=2)
        
    def pomodoro_start(self):
        try:
            #Input provided by user is stored in temp
            temp = int(self.minute.get())*60 + int(self.second.get())
        except:
            print("Please input the correct value")
        while temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)

            # Logic to convert input entered in mins 
    
        
        


root = Tk()
Pomodoro(root)
root.mainloop()