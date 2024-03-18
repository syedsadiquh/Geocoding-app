import tkinter as tk
from tkinter import ttk

from dbConnector import DBConnect


# History Window for the Queries along with the responses.
class HistoryWindow:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(
            master=self.master,
            text="History",
            font=('Helvetica', 21),
            pady=15
        )
        self.label.pack()

        # Database connection
        self.db = DBConnect()
        self.db.create_table()
        self.data = self.db.read_all()
        if len(self.data) != 0:
            self.tree = ttk.Treeview(master=self.master, columns=("c1", "c2", "c3"), show='headings')
            self.tree.column("#1", anchor='w', minwidth=40, width=50)
            self.tree.heading("#1", text="Sl. No.", anchor=tk.CENTER)
            self.tree.column("#2", anchor=tk.CENTER)
            self.tree.heading("#2", text="Query")
            self.tree.column("#3", anchor=tk.CENTER)
            self.tree.heading("#3", text="Response")
            self.tree.pack()
            for row in self.data:
                print(row)
                self.tree.insert("", tk.END, values=row)

            self.clear_button = tk.Button(master=self.master, text="Clear History",
                                          command=self.clr_all_hist)
            self.clear_button.pack()

        else:
            self.empty_label = tk.Label(self.master, text="No Data Found", font=('Helvetica bold', 14))
            self.empty_label.pack()

        self.db.close_connection()

    def clr_all_hist(self):
        db = DBConnect()
        db.clear_all_history()
        db.close_connection()
        self.tree.pack_forget()
        self.clear_button.pack_forget()
        clear_label = tk.Label(master=self.master, text="all History Cleared", font=('Helvetica bold', 16))
        clear_label.pack()
