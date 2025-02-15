import tkinter as tk

# Function to update the expression in the entry box
def button_click(value):
    current_text = entry_box.get()
    entry_box.delete(0, tk.END)
    entry_box.insert(0, current_text + value)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry_box.get())
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(result))
    except Exception as e:
        entry_box.delete(0, tk.END)
        entry_box.insert(0, "Error")

# Function to clear the entry box
def clear():
    entry_box.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create an entry box
entry_box = tk.Entry(root, width=25, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda button=button: button_click(button)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text='C', width=5, height=2, command=clear).grid(row=row, column=col)

# Start the main loop
root.mainloop()
