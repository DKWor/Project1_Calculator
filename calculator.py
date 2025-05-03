
import tkinter as tk

cal=tk.Tk()
cal.geometry("850x400")
cal.title("Scientific Calculator")


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

outer_frame = tk.Frame(cal, bg="black", bd=5, relief="ridge")
outer_frame.pack(fill="both", expand=True, padx=10, pady=10)

entry = tk.Entry(outer_frame, font=("Arial", 20), borderwidth=5, relief="solid", justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, padx=0, pady=1)

button_frame = tk.Frame(outer_frame,bg="lightgray", bd=5, relief="ridge")
button_frame.pack(expand=True, fill="both", ipadx=8, ipady=8, padx=1, pady=1)

# Now adding buttons
buttons = [
    
    ('mod', 0, 0), ('MC', 0, 7), ('MR', 0, 8), ('M+', 0, 9), ('M-', 0, 10),
    ('sinh', 1, 0), ('cosh', 1, 1), ('tanh', 1, 2), ('Exp', 1, 3), ('(', 1, 4), (')', 1, 5), ('←', 1, 6),('C', 1, 7),('+/-', 1, 8),('√', 1, 9),
    ('sinh-1', 2, 0), ('cosh-1', 2, 1), ('tanh-1', 2, 2),('log2x', 2, 3), ('ln', 2, 4), ('log', 2, 5), ('7', 2, 6),('8', 2, 7),('9', 2, 8),('/', 2, 9),('%', 2, 10),
    ('π', 3, 0), ('e', 3, 1), ('n!', 3, 2),('logyx', 3, 3), ('ex', 3, 4), ('10x', 3, 5), ('4', 3, 6),('5', 2, 7),('6', 2, 8),('*', 2, 9),('1/x', 2, 10),
    ('sin', 4, 0), ('cos', 4, 1), ('tan', 4, 2),('xy', 4, 3), ('x3', 4, 4), ('x2', 4, 5), ('1', 4, 6),('2', 4, 7),('3', 4, 8),('-', 4, 9),('=', 4, 10),
    ('sin-1', 5, 0), ('cos-1', 5, 1), ('tan-1', 5, 2),('y√x', 5, 3), ('∛ ', 5, 4), ('|x|', 5, 5), ('0', 5, 6),('.', 5, 7),('+', 5, 8)

]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    colspan = btn[3] if len(btn) == 4 else 1

    action = None
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear_entry
    else:
        action = lambda value=text: button_click(value)

    button = tk.Button(button_frame, text=text, font=("Arial", 18), borderwidth=2, relief="raised", command=action)
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=1, pady=1)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)






cal.mainloop()


