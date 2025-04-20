# Program for adding button widget and initiate messagebox on click.

import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Button Clicked! Hello from Tkinter.")

root = tk.Tk()
root.title("Button and Messagebox Example")

button = tk.Button(root, text="Click Me", command=show_message)

button.pack(pady=20)

root.mainloop()