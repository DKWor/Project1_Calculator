import tkinter as tk
from math import *
import math



def mod(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a % b

memory = 0  # Memory storage
def memory_clear():
    global memory
    memory = 0

def memory_recall():
    entry.insert(tk.END, str(memory))

def memory_store():
    global memory
    try:
        memory = float(entry.get())
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def memory_add():
    global memory
    try:
        memory += float(entry.get())
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def memory_subtract():
    global memory
    try:
        memory -= float(entry.get())
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")



def sinh_func():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, math.sinh(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cosh_func():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, math.cosh(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def tanh_func():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, math.tanh(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def exp_func():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, math.exp(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert_parenthesis(symbol):
    entry.insert(tk.END, symbol)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def clear_entry():
    entry.delete(0, tk.END)

def toggle_sign():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, -value)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sqrt_func():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, math.sqrt(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get().replace('mod', '%')  # convert 'mod' to '%'
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: Division by zero")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

import math

def sinh_inverse():
    try:
        value = float(entry.get())
        result = math.asinh(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cosh_inverse():
    try:
        value = float(entry.get())
        result = math.acosh(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def tanh_inverse():
    try:
        value = float(entry.get())
        result = math.atanh(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def log2_func():
    try:
        value = float(entry.get())
        result = math.log2(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def ln_func():
    try:
        value = float(entry.get())
        result = math.log(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def log10_func():
    try:
        value = float(entry.get())
        result = math.log10(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def percent_func():
    try:
        value = float(entry.get())
        result = value / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def calculate_factorial():
    try:
        value = int(entry.get())
        result = math.factorial(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def prepare_log_base():
    # You might want to show input for base and value separately
    # or assume a format like 'logyx(100, 10)'
    try:
        value = entry.get()
        x, y = map(float, value.split(','))
        result = math.log(x, y)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_exp():
    try:
        x = float(entry.get())
        result = math.exp(x)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_power_10():
    try:
        x = float(entry.get())
        result = 10 ** x
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def calculate_reciprocal():
    try:
        x = float(entry.get())
        if x == 0:
            raise ZeroDivisionError
        result = 1 / x
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_trig(func_name):
    try:
        x = float(entry.get())
        radians = math.radians(x)  # Assuming input is in degrees
        if func_name == 'sin':
            result = math.sin(radians)
        elif func_name == 'cos':
            result = math.cos(radians)
        elif func_name == 'tan':
            result = math.tan(radians)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_power_xy():
    try:
        value = entry.get()
        x, y = map(float, value.split(','))
        result = x ** y
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_power(n):
    try:
        x = float(entry.get())
        result = x ** n
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_inverse_trig(func_name):
    try:
        x = float(entry.get())
        if func_name == 'sin':
            result = math.degrees(math.asin(x))
        elif func_name == 'cos':
            result = math.degrees(math.acos(x))
        elif func_name == 'tan':
            result = math.degrees(math.atan(x))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_root_yx():
    try:
        value = entry.get()
        y, x = map(float, value.split(','))
        if x == 0:
            raise ZeroDivisionError
        result = y ** (1 / x)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_nth_root(n):
    try:
        x = float(entry.get())
        result = x ** (1 / n)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_abs():
    try:
        x = float(entry.get())
        result = abs(x)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
    


# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=11, padx=5, pady=5, sticky="nsew")

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=11)

# Button definitions
buttons = [
    ('mod', 0, 0), ('MC', 0, 6), ('MR', 0, 7), ('MS', 0, 8), ('M+', 0, 9), ('M-', 0, 10),
    ('sinh', 1, 0), ('cosh', 1, 1), ('tanh', 1, 2), ('Exp', 1, 3), ('(', 1, 4), (')', 1, 5), ('←', 1, 6, 1, 2) , ('C', 1, 8), ('+/-', 1, 9), ('√', 1, 10),
    ('sinh-1', 2, 0), ('cosh-1', 2, 1), ('tanh-1', 2, 2), ('log2x', 2, 3), ('ln', 2, 4), ('log', 2, 5), ('7', 2, 6), ('8', 2, 7), ('9', 2, 8), ('/', 2, 9), ('%', 2, 10),
    ('π', 3, 0), ('e', 3, 1), ('n!', 3, 2), ('logyx', 3, 3), ('ex', 3, 4), ('10x', 3, 5), ('4', 3, 6), ('5', 3, 7), ('6', 3, 8), ('*', 3, 9), ('1/x', 3, 10),
    ('sin', 4, 0), ('cos', 4, 1), ('tan', 4, 2), ('xy', 4, 3), ('x3', 4, 4), ('x2', 4, 5), ('1', 4, 6), ('2', 4, 7), ('3', 4, 8), ('-', 4, 9), ('=', 4, 10, 1, 2),
    ('sin-1', 5, 0), ('cos-1', 5, 1), ('tan-1', 5, 2), ('y√x', 5, 3), ('∛', 5, 4), ('|x|', 5, 5), ('0', 5, 6), ('.', 5, 7), ('+', 5, 8, 1, 2)
]

for btn in buttons:
    text = btn[0]
    row = btn[1]
    col = btn[2]
    rowspan = btn[3] if len(btn) > 3 else 1
    colspan = btn[4] if len(btn) > 4 else 1


    if text == "=":
        action = calculate
    elif text == "mod":
        action = lambda: entry.insert(tk.END, 'mod')
    elif text == "←":
        action = lambda: entry.delete(len(entry.get())-1, tk.END)
    elif text == "MC":
        action = memory_clear
    elif text == "MR":
        action = memory_recall
    elif text == "MS":
        action = memory_store
    elif text == "M+":
        action = memory_add
    elif text == "M-":
        action = memory_subtract
    elif text == "sinh":
      action = sinh_func
    elif text == "cosh":
      action = cosh_func
    elif text == "tanh":
      action = tanh_func
    elif text == "Exp":
      action = exp_func
    elif text == "(":
      action = lambda: insert_parenthesis("(")
    elif text == ")":
      action = lambda: insert_parenthesis(")")
    elif text == "←":
      action = backspace
    elif text == "C":
      action = clear_entry
    elif text == "+/-":
      action = toggle_sign
    elif text == "√":
      action = sqrt_func
    elif text == "sinh-1":
      action = sinh_inverse
    elif text == "cosh-1":
      action = cosh_inverse
    elif text == "tanh-1":
      action = tanh_inverse
    elif text == "log2x":
      action = log2_func
    elif text == "ln":
      action = ln_func
    elif text == "log":
      action = log10_func
    elif text == "%":
      action = percent_func
    elif text == "π":
      action = lambda: button_click(str(math.pi))
    elif text == "e":
      action = lambda: button_click(str(math.e))
    elif text == "n!":
      action = lambda: calculate_factorial()
    elif text == "logyx":
      action = lambda: prepare_log_base()
    elif text == "ex":
      action = lambda: calculate_exp()
    elif text == "10x":
      action = lambda: calculate_power_10()
    elif text == "*":
      action = lambda: button_click("*")
    elif text == "1/x":
      action = lambda: calculate_reciprocal()
    elif text == "sin":
      action = lambda: calculate_trig('sin')
    elif text == "cos":
     action = lambda: calculate_trig('cos')
    elif text == "tan":
     action = lambda: calculate_trig('tan')
    elif text == "xy":
     action = lambda: calculate_power_xy()
    elif text == "x3":
     action = lambda: calculate_power(3)
    elif text == "x2":
     action = lambda: calculate_power(2)
    elif text == "-":
     action = lambda: button_click("-")
    elif text == "sin-1":
     action = lambda: calculate_inverse_trig('sin')
    elif text == "cos-1":
     action = lambda: calculate_inverse_trig('cos')
    elif text == "tan-1":
     action = lambda: calculate_inverse_trig('tan')
    elif text == "y√x":
     action = lambda: calculate_root_yx()
    elif text == "∛":
     action = lambda: calculate_nth_root(3)
    elif text == "|x|":
     action = lambda: calculate_abs()
    elif text == ".":
     action = lambda: button_click(".")
    elif text == "+":
     action = lambda: button_click("+")

    else:
      action = lambda value=text: button_click(value)


# Highlight number buttons
    if text.isdigit():
        bg_color = "#0d6efd"  # Light green highlight
    else:
        bg_color = "lightblue"  # Default color
    button = tk.Button(button_frame, text=text, font=("Arial", 12),bg=bg_color,fg="black", borderwidth=5, relief="raised", command=action, width=5, height=2)
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=1, pady=1)
   
    tk.Button(button_frame, text="=", font=("Arial", 12),bg="#8B0000",fg="white", width=5, height=2, command=calculate)\
    .grid(row=4, column=10, rowspan=2, sticky="nsew", padx=1, pady=1)
  
   

    
# Expand rows and columns for uniform layout
for i in range(12):
    button_frame.columnconfigure(i, weight=1)
for i in range(6):
    button_frame.rowconfigure(i, weight=1)

root.mainloop()
