import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter RadioButton Example")
root.geometry("300x200")

# Variable to store selected option
selected_option = tk.StringVar(value="None")

# Function to display the selected option
def show_selection():
    label.config(text=f"Selected: {selected_option.get()}")

# Creating RadioButtons
radio1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1", command=show_selection)
radio2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2", command=show_selection)
radio3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3", command=show_selection)

# Displaying RadioButtons
radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Label to show selected option
label = tk.Label(root, text="Selected: None")
label.pack(pady=10)

# Run the main event loop
root.mainloop()