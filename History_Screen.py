import tkinter as tk


# History Window for the Queries along with the responses.
class HistoryWindow:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master=self.master, text="HELLO WORLD", font=('Helvetica', 21))
        self.label.pack()
