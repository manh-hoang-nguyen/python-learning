import tkinter as tk
from tkinter import ttk

def button_func():
    print(entry.get())
    entry_text = entry.get()
    # update label
    label.config(text=entry_text) # = lable['text'] = "new text label"
    entry['state'] = 'disabled'
    

def excercise_button_func():
    label.config(text='some text')
    entry['state'] = 'enabled'
    entry.delete(0, 'end')
    
window = tk.Tk()
window.title("Getting and Setting widgets")
window.geometry('300x200')
# widgets
label = ttk.Label(master=window, text="some text label")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="The button", command=button_func)
button.pack()

# exercise: add another button that changes text back to 'some text' and that enables entry

excercise_button = ttk.Button(master=window, text='reset',command=excercise_button_func)
excercise_button.pack()
window.mainloop()
