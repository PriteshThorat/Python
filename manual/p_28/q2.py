import tkinter as tk

# Create main application window
root = tk.Tk()
root.title("Tkinter CheckButton Example")
root.geometry("300x200")

# Variable to store CheckButton state
var = tk.IntVar()  # 1 if checked, 0 if unchecked

# Function to display CheckButton state
def show_state():
    state = "Checked" if var.get() == 1 else "Unchecked"
    label.config(text=f"Status: {state}")

# Creating a CheckButton
check_button = tk.Checkbutton(root, text="Accept Terms", variable=var, command=show_state)
check_button.pack(pady=10)

# Label to display state
label = tk.Label(root, text="Status: Unchecked")
label.pack(pady=10)

# Run the application
root.mainloop()