import tkinter as tk
from tkinter import messagebox

import geocoding_main as gc
from geocoding_main import QueryError
from dbConnector import DBConnect

from History_Screen import HistoryWindow


# This is the staring part of the 'APP'.
class Application:
    def __init__(self, master):
        self.master = master
        self.forward = False  # Variable for switching modes.
        self.history_window = ""

        self.welcome_txt = tk.Label(
            master=self.master,
            text="Welcome to Geocoding",
            pady=20,
            font=('Helvetica bold', 26),
        )
        self.welcome_txt.pack()

        self.heading_frame = tk.Frame(self.master)
        # Guide to text for the Geocoding mode
        self.geocoding_mode_text = tk.Label(
            master=self.heading_frame,
            text="Current Geocoding mode : "
        )
        self.geocoding_mode_text.grid(row=2)

        # Current Geocoding Mode
        self.geocoding_mode = tk.Label(
            master=self.heading_frame,
            padx=5,
            text="Forward Geocoding",
            font=('Helvetica bold', 14)
        )
        self.geocoding_mode.grid(row=2, column=2)

        # Switch Button for switching between mode
        self.switch_button = tk.Button(
            master=self.heading_frame,
            text="Switch",
            padx=10,
            command=self.button_mode
        )
        self.switch_button.grid(row=2, column=4)
        self.heading_frame.pack()

        # History button.
        self.history_button = tk.Button(
            master=self.master,
            text="History",
            height=1,
            width=10,
            command=self.open_history
        )
        self.history_button.pack(anchor='w', padx=150)

        # Frame for Forward Geocoding.
        self.f_frame = tk.Frame(master=self.master, pady=30)
        self.f_geo = ForwardGeocoding(self.f_frame)
        self.f_frame.pack()

        # Frame for Reverse Geocoding.
        self.r_frame = tk.Frame(master=self.master, pady=30)
        self.r_geo = ReverseGeocoding(master=self.r_frame)

    # Opens a new window for the History.
    def open_history(self):
        self.history_window = tk.Toplevel()
        self.history_window.title("History")
        self.history_window.geometry("500x350")
        _ = HistoryWindow(self.history_window)
        self.history_window.mainloop()

    # This method is for Switching modes
    def button_mode(self):
        # Determine it is on or off
        if self.forward:
            self.geocoding_mode.config(text="Forward Geocoding")
            self.r_frame.pack_forget()
            self.f_frame.pack()
            self.forward = False
        else:
            self.geocoding_mode.config(text="Reverse Geocoding")
            self.f_frame.pack_forget()
            self.r_frame.pack()
            self.forward = True


# This Class is for the Forward Geocoding widget
class ForwardGeocoding:
    def __init__(self, master):
        self.master = master
        self.lat_lng = []
        self.address_label = tk.Label(master=self.master, text="Address:", font=('Helvetica bold', 16))
        self.address_label.grid(row=0, column=2, sticky=tk.W)
        self.address_box = tk.Text(master=self.master, width=30, height=10)
        self.address_box.grid(row=1, column=2)
        self.address_button = tk.Button(
            master=self.master,
            text="Convert",
            command=self.get_address
        )
        self.address_button.grid(row=2, column=2)
        self.result_label = tk.Label(self.master, text="Geographical Coordinates:", font=('Helvetica bold', 16))
        self.result_label.grid(row=0, column=4, padx=50)

        # Frame to hold the results
        self.lat_lng_frame = tk.Frame(master=self.master)
        self.lat_label = tk.Label(master=self.lat_lng_frame, text="Latitude:")
        self.lat_label.grid(row=0, column=0, sticky=tk.W)
        self.lat = tk.Label(master=self.lat_lng_frame, text="N/A")
        self.lat.grid(row=0, column=1, sticky=tk.W)

        self.lng_label = tk.Label(master=self.lat_lng_frame, text="Longitude:")
        self.lng_label.grid(row=1, column=0, sticky=tk.W)
        self.lng = tk.Label(master=self.lat_lng_frame, text="N/A")
        self.lng.grid(row=1, column=1, sticky=tk.W)

        self.lat_lng_frame.grid(row=1, column=4, pady=20, sticky=tk.N)

    def get_address(self):
        try:
            self.lat_lng = gc.forward_geocode_results(self.address_box.get("1.0", "end-1c"), gc.API_KEY)
            self.lat.config(text=str(self.lat_lng[0]))
            self.lng.config(text=str(self.lat_lng[1]))
            db = DBConnect()
            db.create_table()
            # Checking if the given address is already present in the db as query
            present_in_db = False
            for row in db.read_all():
                if self.address_box.get("1.0", "end-1c") in row:
                    present_in_db = True
            # Adding in db only if the address in not present in db as query
            if not present_in_db:
                db.insert_into_table(
                    _query=self.address_box.get("1.0", "end-1c"),
                    _response=str([self.lat_lng[0], self.lat_lng[1]])
                )
            db.close_connection()
            # Clearing the Address Box after submitting
            self.address_box.delete('1.0', 'end')

        except ConnectionError as ce:
            messagebox.showerror(title="Error!", message=str(ce), icon='error')
        except QueryError as qe:
            messagebox.showerror(title="Error!", message=qe.message, icon='error')


# This Class is for the Reverse Geocoding widget
class ReverseGeocoding:
    def __init__(self, master):
        self.master = master
        self.address = ""
        # Entry area for the latitude and the longitude
        self.entry_frame = tk.Frame(master=self.master)
        self.lat_label = tk.Label(master=self.entry_frame, text="Latitude:", font=('Helvetica bold', 16))
        self.lat_label.grid(row=0, column=0, sticky=tk.W)
        self.lat_entry = tk.Entry(master=self.entry_frame, width=30)
        self.lat_entry.grid(row=1, column=0)
        # Empty Text Label for space between input fields only.
        self.space_label = tk.Label(master=self.entry_frame, text="", pady=5)
        self.space_label.grid(row=2, column=0)
        self.lng_label = tk.Label(master=self.entry_frame, text="Longitude:", font=('Helvetica bold', 16))
        self.lng_label.grid(row=3, column=0, sticky=tk.W)
        self.lng_entry = tk.Entry(master=self.entry_frame, width=30)
        self.lng_entry.grid(row=4, column=0)
        self.convert_button = tk.Button(
            master=self.entry_frame,
            text="Convert",
            command=self.get_address
        )
        self.convert_button.grid(row=5, column=0)
        self.entry_frame.grid(row=0, column=2)
        # Result area of the Formatted Address.
        self.result_label = tk.Label(master=self.master, text="Address:", font=('Helvetica bold', 16))
        self.result_label.grid(row=0, column=4, padx=50, sticky=tk.NW)
        self.address_frame = tk.Frame(master=self.master)
        self.address_label = tk.Label(master=self.address_frame, text="", wraplength=150, justify='left')
        self.address_label.grid(row=0, column=0, sticky=tk.NW)
        self.address_frame.grid(row=0, column=4, padx=30, pady=30)

    def get_address(self):
        try:
            self.address = gc.reverse_geocode_results(self.lat_entry.get(), self.lng_entry.get(), gc.API_KEY)
            self.address_label.config(text=str(self.address))
            db = DBConnect()
            db.create_table()
            # Checking if the [lat,lng] is already present in history/db
            present_in_db = False
            for row in db.read_all():
                if str([self.lat_entry.get(), self.lng_entry.get()]) in row:
                    present_in_db = True
                    break
            # Inserting [lat,lng] into table only when it is not present in db as query
            if not present_in_db:
                db.insert_into_table(_query=str([self.lat_entry.get(), self.lng_entry.get()]),
                                     _response=str(self.address))
            db.close_connection()
            # clearing the Entry box at the end.
            self.lat_entry.delete(0, tk.END)
            self.lng_entry.delete(0, tk.END)

        except ConnectionError as ce:
            messagebox.showerror(title="Error!", message=str(ce), icon='error')
        except QueryError as qe:
            messagebox.showerror(title="Error!", message=qe.message, icon='error')


def main():
    root = tk.Tk()
    root.geometry("720x420")
    root.title("Geo-Coding")
    root.iconphoto(False, tk.PhotoImage(file="Assets/Icons/globe_icon.png"))
    _ = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
