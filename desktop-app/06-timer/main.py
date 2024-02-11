import customtkinter as ctk
import datetime
import time
import tkinter as tk


class App(ctk.CTk):
    ctk.set_appearance_mode("dark")

    def __init__(self):
        super().__init__()
        self.title = "Timer"
        self.geometry("200x350")

        self.rowconfigure(0, weight=3, uniform="a")
        self.rowconfigure(1, weight=3, uniform="a")
        self.columnconfigure(0, weight=1)
        Clock(self)
        ButtonConfigs(self)


class ButtonConfigs(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=1, column=0)
        timer = Timer()
        btn_start = ctk.CTkButton(self, text="Start", command=lambda: timer.start())
        btn_pause = ctk.CTkButton(self, text="Pause", command=lambda: timer.pause())
        btn_start.pack()
        btn_pause.pack()


class Timer:
    def __init__(self):
        self.timer = 0
        self.is_running = False

    def start(self):
        print("timer start")
        self.is_running = True

    def pause(self):
        print("timer pause")
        self.is_running = False

    def reset(self):
        print("timer reset")
        self.is_running = False
        self.timer = 0

    def resume(self):
        print("timer resume")
        self.is_running = True


class Clock(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, background="black")
        self.grid(row=0, column=0)

        self.bind("<Configure>", self.win_resize)

    def win_resize(self, event):
        self.center = (event.width / 2, event.height / 2)
        self.size = (event.width, event.height)

    def draw(self,milliseconds=0):
        self.draw_center()

    def draw_center(self):
        pass
if __name__ == "__main__":
    app = App()
    app.mainloop()
