import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Tkinter Menu Example")
root.geometry("400x300")

# Function to handle menu actions
def show_message(msg):
    messagebox.showinfo("Menu Action", msg)

# Create a Menu bar
menu_bar = tk.Menu(root)

# Create "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: show_message("New File Created"))
file_menu.add_command(label="Open", command=lambda: show_message("File Opened"))
file_menu.add_command(label="Save", command=lambda: show_message("File Saved"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: show_message("Cut Action"))
edit_menu.add_command(label="Copy", command=lambda: show_message("Copy Action"))
edit_menu.add_command(label="Paste", command=lambda: show_message("Paste Action"))

# Create "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: show_message("Tkinter Menu Example"))

# Add menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Attach the menu to the root window
root.config(menu=menu_bar)

# Run the application
root.mainloop()