import tkinter as tk
from tkinter import ttk

def on_click():
    label.config(text="Hello, World!")

# Create main window
root = tk.Tk()
root.title("Hello World App")
root.geometry("300x200")

# Create a label
label = ttk.Label(root, text="Click the button", font=('Arial', 14))
label.pack(pady=20)

# Create a button
button = ttk.Button(root, text="Greet", command=on_click)
button.pack()

# Run the application
root.mainloop()