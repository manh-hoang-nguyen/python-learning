import customtkinter as ctk
import os
from tkinter import *
from settings import *
from PIL import Image, ImageTk

DIR_NAME = os.path.dirname(os.path.realpath(__file__))


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("light")
        super().__init__()
        self.title("Paint")
        self.iconbitmap(
            f"{os.path.dirname(os.path.realpath(__file__))}/empty.ico")
        self.geometry("800x600")
        self.color_string_var = ctk.StringVar(value="black")
        self.color_string_var.trace_add("write", self.color_change)
        # widget
        self.draw_surface = DrawSurface(
            self, circle_radius=10, color_string=self.color_string_var.get())
        ToolPanel(self)

    def color_change(self, event, *args):
        print("color change")

    def draw(self):
        print("draw")

    def erase(self):
        self.color_string_var.set("white")
        self.draw_surface.set_corlor('white')

    def clear(self):
        print("clear")


class ToolPanel(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent, width=200, height=300)
        self.iconbitmap(
            f"{os.path.dirname(os.path.realpath(__file__))}/empty.ico")
        self.attributes("-topmost", True)
        self.rowconfigure(0, weight=2, uniform="a")
        self.rowconfigure(1, weight=3, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")
        self.rowconfigure(3, weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="b")
        # data
        self.action_type_string = ctk.StringVar()

        # widget
        ActionType(
            self,
            draw_func=parent.draw,
            erase_func=parent.erase,
            clear_func=parent.clear,
        )


class ActionType(ctk.CTkFrame):
    def __init__(self, parent, draw_func, erase_func, clear_func):
        super().__init__(parent)
        self.grid(row=3, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1, uniform="c")
        self.columnconfigure(1, weight=1, uniform="c")
        self.columnconfigure(2, weight=1, uniform="c")
        self.rowconfigure(0, weight=1, uniform="a")
        Button(self, f"{DIR_NAME}/images/brush.png", 0, 0, draw_func)
        Button(self, f"{DIR_NAME}/images/eraser.png", 0, 1, erase_func)
        Button(self, f"{DIR_NAME}/images/clear.png", 0, 2, clear_func)


class Button(ctk.CTkButton):
    def __init__(self, parent, image_path, row, column, func):
        draw_image = Image.open(image_path).resize((20, 20))
        draw_imagetk = ctk.CTkImage(draw_image)
        super().__init__(
            parent,
            text="",
            image=draw_imagetk,
            hover_color=BUTTON_HOVER_COLOR,
            command=func,
        )
        self.grid(row=row, column=column, sticky="nswe")


class DrawSurface(Canvas):
    def __init__(self, parent, circle_radius, color_string):
        super().__init__(parent, background=CANVS_BG, highlightthickness=0)
        self.circle_radius = circle_radius
        self.color_string = color_string
        self.pre_point = None
        self.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.bind("<Motion>", self.motion)

    def motion(self, event):
        center_x, center_y = event.x, event.y
        if self.pre_point is not None:
            print("create line")
            self.create_line(
                self.pre_point.x,
                self.pre_point.y,
                event.x,
                event.y,
                fill=self.color_string,
                width=self.circle_radius,
                capstyle='round'
            )
        else:
            
            self.create_oval(
                center_x - self.circle_radius,
                center_y - self.circle_radius,
                center_x + self.circle_radius,
                center_y + self.circle_radius,
                fill=self.color_string,
            )
        self.pre_point = event

    def set_corlor(self, color_string):
        self.color_string = color_string


if __name__ == "__main__":
    app = App()
    app.mainloop()
