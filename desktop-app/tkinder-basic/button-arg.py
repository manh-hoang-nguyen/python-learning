import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print(entry_string.get())

window = tk.Tk()
window.title("Button with arguments")

entry_var = tk.StringVar(value="initial value")

entry=ttk.Entry(master=window, textvariable=entry_var)
entry.pack()

button = ttk.Button(master=window,text="Set value",command= lambda: button_func(entry_var))
button.pack()

# note: we can use inner fucntion to replace lambda function
def outer_func(parameter):
    def inner_func():
        print(parameter.get())
    return inner_func
window.mainloop()