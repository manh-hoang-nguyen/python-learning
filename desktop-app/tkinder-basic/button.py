import tkinter as tk
from tkinter import ttk


def button_func():
    print('basic button')


window = tk.Tk()
window.title("Button")
window.geometry('300x200')

# basic button
button_string_var = tk.StringVar(value='A button with string var')
button = ttk.Button(master=window, text="basic button",
                    command=button_func, textvariable=button_string_var)
button.pack()

# check button
check_var = tk.IntVar()
check = ttk.Checkbutton(
    master=window, 
    text='checkbox 1',
    command=lambda: print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5)
check.pack()
check2 = ttk.Checkbutton(
    master=window, 
    text='checkbox 2',
    command=lambda:  check_var.set(5))
check2.pack()
# radio button
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    master=window, 
    text='radiobutton 1',
    variable=radio_var, 
    value="radio 1", 
    command= lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    master=window, 
    text='radiobutton 2', 
    value=2,
    variable=radio_var
    )
radio2.pack()


window.mainloop()
