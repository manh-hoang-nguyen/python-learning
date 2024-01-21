import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Variables")
window.geometry('300x200') 


# variables
string_var = tk.StringVar()

#widgets
label = ttk.Label(master=window, textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window,textvariable=string_var)
entry.pack()




#excercise: create 2 entry fields and 1 labels, the shoud all be connected via a stringvar & set a start value of test

string_var_exe= tk.StringVar(value='test')


entry1 = ttk.Entry(master=window,textvariable=string_var_exe)
entry1.pack()
entry2 = ttk.Entry(master=window,textvariable=string_var_exe)
entry2.pack()
label_exe = ttk.Label(master=window, textvariable=string_var_exe)
label_exe.pack()






window.mainloop()