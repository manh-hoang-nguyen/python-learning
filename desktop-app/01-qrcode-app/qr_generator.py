import tkinter as tk
import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk, ImageDraw
import os
from tkinter import filedialog

class EntryField(ctk.CTkFrame):
    def __init__(self, parent, entry_string, save_func):
        super().__init__(parent, corner_radius=20, fg_color="#021FB3")
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")

        # Grid layout
        self.rowconfigure((0, 1), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")

        # widgets
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.columnconfigure(0, weight=1, uniform="b")
        self.frame.columnconfigure(1, weight=4, uniform="b")
        self.frame.columnconfigure(2, weight=2, uniform="b")
        self.frame.columnconfigure(3, weight=1, uniform="b")
        self.frame.grid(row=0, column=0)
        self.entry = ctk.CTkEntry(
            self.frame,
            fg_color="#2E54E8",
            border_width=0,
            text_color="white",
            placeholder_text="write some texts",
            textvariable=entry_string,
        )
        self.entry.grid(row=0, column=1, sticky="nsew")
        button = ctk.CTkButton(
            self.frame,
            text="save",
            fg_color="#2E54E8",
            hover_color="#4266f1",
            command=save_func,
        )
        button.grid(row=0, column=2, sticky="nsew", padx=10)

    def reset(self):
        self.entry.delete(0, "end")


class QrImage(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, background="white")
        self.place(relx=0.5, rely=0.4, width=200, height=200, anchor="center")

    def update_image(self, image_tk):
        self.clear()
        self.create_image(0, 0, image=image_tk, anchor="nw")


class App(ctk.CTk):
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)

    def __init__(self, title, size):
        # Window set up
        ctk.set_appearance_mode("light")
        super().__init__()

        # Custumization
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        # self.iconbitmap(f"{self.script_directory}/empty.ico")
        self.wm_attributes('-toolwindow', 'True') # Remove icon window

        # Entry Field
        self.entry_string = ctk.StringVar()
        self.entry_string.trace_add("write", self.create_qr)
        self.entry_field = EntryField(self, self.entry_string, self.save_image)

        # Event
        self.bind("<Return>", self.save_image)

        # QR code
        self.raw_image = None
        self.tk_image = None
        self.qr_image = QrImage(self)

    def create_qr(self, *args):
        current_text = self.entry_string.get()
        if current_text:
            self.raw_image = qrcode.make(current_text).resize((200, 200))
            self.tk_image = ImageTk.PhotoImage(self.raw_image)
            self.qr_image.update_image(self.tk_image)
        else:
            self.qr_image.clear()
            self.raw_image = None
            self.tk_image = None
            self.qr_image.clear()

    def save_image(self, event=""):
        if self.raw_image:
            filepath = filedialog.asksaveasfilename()
            if filepath:
                self.raw_image.save(filepath + ".png")
                self.entry_field.reset()


app = App("QR Code generator", (400, 400))
app.mainloop()
