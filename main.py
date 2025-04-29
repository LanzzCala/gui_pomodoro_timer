from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

class Pomodoro:
    def __init__(self, root):
        self.root = root
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
        self.hour = StringVar()
        self.minute = StringVar()
        self.second = StringVar()

        #Set default value of numbers to 0
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")
        hour_entry = ttk.Entry(mainframe, width=6, font=(15), textvariable=self.hour)
        hour_entry.grid(column=1, row=2)
        minute_entry = ttk.Entry(mainframe, width=6, font=(15), textvariable=self.minute)
        minute_entry.grid(column=2, row=2)
        second_entry = ttk.Entry(mainframe, width=6, font=(15), textvariable=self.second)
        second_entry.grid(column=3, row=2)
        
    def pomodoro_start(self):
        try:
            #Input provided by user is stored in temp
            temp = int(self.hour.get())*3600 + int(self.minute.get())*60 + int(self.second.get())
        except:
            print("Please input the correct value")
        while temp >-1:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)

            # Logic to convert input entered in mins or secs to hours,
            # mins, secs (input = 110 min --> 120 * 60 = 6600 => 1 Hr : 50 # Min: 0 sec)
            hours = 0
            if mins > 60:

                # divmod (firstvalue = temp//60, secondvalue = temp%60)
                hours, mins = divmod(mins, 60)

            # using format () method to store the value up to two decimal places
            self.hour.set("{0:2d}".format(hours))
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))

            # Update GUI window after decrementing the temp value every time
            self.root.update()
            time.sleep(1)

            # when temp value = 0; messagebox pops up message "time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")

            #after every one sec, value of temp will decrement
            temp -= 1
        
        


root = Tk()
Pomodoro(root)
root.mainloop()