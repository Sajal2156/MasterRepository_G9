import tkinter as tk

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def append_to_display(value):
    entry.insert(tk.END, value)

def clear_display():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: append_to_display(t))
    button.grid(row=row, column=column)

clear_button = tk.Button(root, text='C', padx=20, pady=10, command=clear_display)
clear_button.grid(row=5, column=0, columnspan=3)

equal_button = tk.Button(root, text='=', padx=20, pady=10, command=evaluate_expression)
equal_button.grid(row=5, column=3)

root.mainloop()
