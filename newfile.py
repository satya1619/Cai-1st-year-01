import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Simple Arithmetic Calculator")
root.geometry("300x300")

# Labels and entry boxes
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons for each operation
tk.Button(root, text="Add (+)", command=lambda: calculate('+')).pack(pady=5)
tk.Button(root, text="Subtract (-)", command=lambda: calculate('-')).pack(pady=5)
tk.Button(root, text="Multiply (*)", command=lambda: calculate('*')).pack(pady=5)
tk.Button(root, text="Divide (/)", command=lambda: calculate('/')).pack(pady=5)

# Label to display result
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

# Run the GUI
root.mainloop()