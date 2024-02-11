from io import BytesIO
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import threading
import ifcopenshell


def start_pb():
    pb.start()
    thread = threading.Thread(target=open_ifc_file)
    thread.start()


def open_ifc_file():
    ifc_file_path = r"C:\Users\mh.nguyen\Downloads\TUN_Tunnel _L16 L1_ MOE_ENT TBM1 _3302P-SDP__Sec11 #2(1).ifc"
    # ifcopenshell.open(ifc_file_path)
    t = open(ifc_file_path, "r")
    data = t.read().splitlines()
    total_line = len(data)
    for index, line in enumerate(data):
        progress_var.set((index+1)/total_line*100)

    print("finish")


def stop_pb():
    pass


def start_pb_thread():
    thread1 = threading.Thread(target=start_pb)
    thread1.start()


win = tk.Tk()

win.title("progress bar")
win.geometry("400x200")
progress_var = tk.IntVar()
pb = ttk.Progressbar(win, maximum=100, variable=progress_var, length=300)
pb.pack()

Button(win, text="start", command=start_pb_thread).pack(pady=20)
Button(win, text="stop", command=stop_pb).pack(pady=20)

win.mainloop()
