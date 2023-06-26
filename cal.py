import math
from tkinter import *

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def clear():
    entry.delete(0, END)

def insert_text(text):
    entry.insert(END, text)

def calculate_function(func):
    try:
        num = float(entry.get())
        result = func(math.radians(num))
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.geometry("300x400")
root.title("Scientific Calculator")

entry = Entry(root, font="Helvetica 14")
entry.pack(fill=X, padx=10, pady=10)

button_frame = Frame(root)
button_frame.pack(padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons dynamically
for i, btn in enumerate(buttons):
    if i % 4 == 3:
        button = Button(button_frame, text=btn, width=5, relief="ridge")
        button.grid(row=i//4, column=i%4)
        button.configure(command=lambda b=btn: insert_text(b))
    else:
        button = Button(button_frame, text=btn, width=5, relief="ridge")
        button.grid(row=i//4, column=i%4)
        button.configure(command=lambda b=btn: insert_text(b))

# Additional buttons
button_pi = Button(button_frame, text='π', width=5, relief="ridge")
button_pi.grid(row=4, column=0)
button_pi.configure(command=lambda: insert_text(str(math.pi)))

button_e = Button(button_frame, text='e', width=5, relief="ridge")
button_e.grid(row=4, column=1)
button_e.configure(command=lambda: insert_text(str(math.e)))

button_clear = Button(button_frame, text='C', width=5, relief="ridge")
button_clear.grid(row=4, column=2)
button_clear.configure(command=clear)

button_equal = Button(button_frame, text='=', width=5, relief="ridge")
button_equal.grid(row=4, column=3)
button_equal.configure(command=evaluate)

# Additional scientific buttons
scientific_functions = [
    ('√', lambda x: math.sqrt(x)),
    ('sin', lambda x: math.sin(x)),
    ('cos', lambda x: math.cos(x)),
    ('tan', lambda x: math.tan(x))
]

for i, (label, func) in enumerate(scientific_functions):
    button_func = Button(button_frame, text=label, width=5, relief="ridge")
    button_func.grid(row=5, column=i)
    button_func.configure(command=lambda f=func: calculate_function(f))

root.mainloop()
