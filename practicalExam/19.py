# Program using label and Radiobutton.

import tkinter as tk

# Function to update label based on radio button selection
def update_label():
    label.config(text="You selected: " + var.get())

# Create the main window
root = tk.Tk()
root.title("Label and Radiobutton Example")

# Create a label
label = tk.Label(root, text="Please select an option", font=('Arial', 14))
label.pack(pady=20)

# Create a Tkinter variable to store the selected option
var = tk.StringVar()

# Create the radiobuttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=update_label)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=update_label)
radio2.pack()

radio3 = tk.Radiobutton(root, text="Option 3", variable=var, value="Option 3", command=update_label)
radio3.pack()

# Start the Tkinter event loop
root.mainloop()