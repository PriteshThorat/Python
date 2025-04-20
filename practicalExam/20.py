# Program using label and Check button.

import tkinter as tk

# Function to update the label based on the selected checkbuttons
def update_label():
    selected = []
    if var1.get():
        selected.append("Option 1")
    if var2.get():
        selected.append("Option 2")
    if var3.get():
        selected.append("Option 3")
    
    label.config(text="You selected: " + ", ".join(selected) if selected else "No options selected")

# Create the main window
root = tk.Tk()
root.title("Label and Checkbutton Example")

# Create a label
label = tk.Label(root, text="Please select your options", font=('Arial', 14))
label.pack(pady=20)

# Create variables to hold the state of each checkbutton
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

# Create checkbuttons
check1 = tk.Checkbutton(root, text="Option 1", variable=var1, command=update_label)
check1.pack()

check2 = tk.Checkbutton(root, text="Option 2", variable=var2, command=update_label)
check2.pack()

check3 = tk.Checkbutton(root, text="Option 3", variable=var3, command=update_label)
check3.pack()

# Start the Tkinter event loop
root.mainloop()