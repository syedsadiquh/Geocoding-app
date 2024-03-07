import tkinter as tk

class Application:
    def __init__(self, master):
        self.master = master
        self.heading_frame = tk.Frame(self.master)
        self.forward = False
        
        self.welcome_txt = tk.Label(
            text="Welcome to Geocoding",
            pady=20,
            font=('Helvetica bold', 26),
        )
        self.welcome_txt.pack()
        
        # Guide text for the Geocoding mode
        self.geocoding_mode_text = tk.Label(
            master=self.heading_frame,
            text="Current Geocoding mode : "
        )
        self.geocoding_mode_text.grid(row=2)
        
        # Current Geocoding Mode
        self.geocoding_mode = tk.Label(
            master=self.heading_frame,
            padx=5,
            text="Forward Geocoding"
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
    # This method is for Switching modes
    def button_mode(self):
        global forward
        # Determine it is on or off
        if self.forward:
            self.geocoding_mode.config(text="Forward Geocoding")
            # reverse_frame.pack_forget()
            # forward_frame.pack()
            self.forward = False
        else:
            self.geocoding_mode.config(text="Reverse Geocoding")
            # forward_frame.pack_forget()
            # reverse_frame.pack()
            self.forward = True

def main():
    root = tk.Tk()
    root.geometry("720x520")
    root.title("Geo-Coding")
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()