from tkinter import *
from tkinter import ttk, messagebox

class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.pack(padx=10, pady=65)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.minsize(400, 200)
        root.maxsize(400, 200)

        # State tracking
        self.running = False
        self.paused = False
        self.remaining_seconds = 0

        # Buttons
        ttk.Button(mainframe, text="Pomodoro", command=self.pomodoro).grid(column=1, row=1, sticky=(N, W))
        ttk.Button(mainframe, text="Short break", command=self.short_break).grid(column=2, row=1, sticky=(N))
        ttk.Button(mainframe, text="Long break", command=self.long_break).grid(column=3, row=1, sticky=(S, W))
        ttk.Button(mainframe, text="Start", command=self.start).grid(column=1, row=3, sticky=(S, E))
        ttk.Button(mainframe, text="Reset", command=self.reset).grid(column=3, row=3, sticky=(S, W))
        ttk.Button(mainframe, text="Pause", command=self.pause).grid(column=2, row=3)

        # Time entry fields
        self.hour = StringVar(value="00")
        self.minute = StringVar(value="00")
        self.second = StringVar(value="00")

        ttk.Entry(mainframe, width=6, font=(15), textvariable=self.hour).grid(column=1, row=2)
        ttk.Entry(mainframe, width=6, font=(15), textvariable=self.minute).grid(column=2, row=2)
        ttk.Entry(mainframe, width=6, font=(15), textvariable=self.second).grid(column=3, row=2)

    #Start button logic
    def start(self):
        if not self.running:
            try:
                self.remaining_seconds = int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 + int(self.second.get())
                self.running = True
                self.paused = False
                self.countdown()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers for the timer.")

    #Countdown button logic
    def countdown(self):
        if self.running and not self.paused:
            if self.remaining_seconds <= 0:
                messagebox.showinfo("Time Countdown", "Time's up!")
                self.running = False
                return

            mins, secs = divmod(self.remaining_seconds, 60)
            hours, mins = divmod(mins, 60)

            self.hour.set(f"{hours:02}")
            self.minute.set(f"{mins:02}")
            self.second.set(f"{secs:02}")

            self.remaining_seconds -= 1
            self.root.after(1000, self.countdown)
    #Pause button logic
    def pause(self):
        if self.running:
            self.paused = not self.paused
            if not self.paused:
                self.countdown()  # Resume
    #Reset button logic
    def reset(self):
        self.running = False
        self.paused = False
        self.remaining_seconds = 0
        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

    def pomodoro(self):
        self.hour.set("00")
        self.minute.set("25")
        self.second.set("00")

    def short_break(self):
        self.hour.set("00")
        self.minute.set("05")
        self.second.set("00")

    def long_break(self):
        self.hour.set("00")
        self.minute.set("15")
        self.second.set("00")


root = Tk()
Pomodoro(root)
root.mainloop()
