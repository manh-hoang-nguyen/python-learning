import tkinter
import time
import threading


def run_thread():
    thread = threading.Thread(target=func)
    thread.start()


def func():
    time.sleep(10)
    print("after 10 second")


window = tkinter.Tk()
window.geometry("200x200")
label = tkinter.Label(master=window, text="Hello")
label.pack()

button = tkinter.Button(master=window, text="press me", command=run_thread)
button.pack()

window.mainloop()
