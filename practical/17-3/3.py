import tkinter as tk

root = tk.Tk()
tk.Label(root, text="Enter First Number: ", justify=tk.LEFT, padx=20).grid(row=0)
firstName = tk.Entry(root)
firstName.grid(row=0, column=1)
tk.Label(root, text="Enter Second Number: ", justify=tk.LEFT, padx=20).grid(row=1)
secondName = tk.Entry(root)
secondName.grid(row=1, column=1)
subBtn = tk.Button(root, text="Sub").grid(row=4, column=0, sticky=tk.W)
addBtn = tk.Button(root, text="Add").grid(row=4, column=1, sticky=tk.W)

result = 0

def add():
  result = firstNumber + secondNumber
  

def sub():
  result = firstNumber - secondNumber

tk.Label(root, text=result, justify=tk.LEFT, padx=20).grid(row=5)
  

#tk.Label(root, text=result, justify=tk.LEFT, padx=20).grid(row=6)
root.mainloop()