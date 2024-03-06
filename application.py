import tkinter as tk

window = tk.Tk(className=" Geo-Coder")
top_frame = tk.Frame(height=200, width= 200)
frame_b = tk.Frame(height=200, width= 200)

forward = False
def button_mode():
    global forward

    # Determine it is on or off
    if forward:
        geocoding_mode.config(text="Forward Geocoding Enabled.")
        button.config(text="Reverse")
        forward = False
    else:
        geocoding_mode.config(text="Reverse Geocoding Enabled.")
        button.config(text="Forward")
        forward = True

welcome_txt = tk.Label(
    master=top_frame,
    text="Welcome to Geocoding",
)

geocoding_mode = tk.Label(
    master=top_frame,
    text="Forward Geocoding Enabled."
)

button = tk.Button(
    master= frame_b,
    text="Reverse",
    bg="black",
    command=button_mode
)
welcome_txt.pack()
geocoding_mode.pack()
button.pack()

top_frame.pack()
frame_b.pack()

window.mainloop()
