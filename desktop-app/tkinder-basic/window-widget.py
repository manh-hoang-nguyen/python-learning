import tkinter as tk
from tkinter import ttk

def button_func():
    print("button pressed")

def exercise_button_func():
    print("hello")
# create a window
window = tk.Tk()
window.title("Window and widgets")
window.geometry('800x500')

# create widgets
text = tk.Text(master=window)
text.pack()

#ttk widgets
label = ttk.Label(master=window,text='hello Hoang')
label.pack()

#ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window, text="presse me", command=button_func)
button.pack()

# excercise
exercise_button = ttk.Button(master=window, text="exercise button",command=exercise_button_func)
exercise_button.pack()

# run
window.mainloop()
