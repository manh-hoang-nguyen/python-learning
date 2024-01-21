import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
import os


class EntryField(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,corner_radius=20,fg_color='#021FB3')
        self.place(relx=0.5, rely=1, relwidth=1,
                   relheight=0.4, anchor='center')
        
        # Grid layout
        self.rowconfigure((0,1),weight=1,uniform='a')
        entry = ctk.CTkEntry(self, placeholder_text="write some texts")
        entry.pack()


class App(ctk.CTk):
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)

    def __init__(self, title, size):
        # Window set up
        ctk.set_appearance_mode("light")
        super().__init__()

        # Custumization
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        self.iconbitmap(f'{self.script_directory}/empty.ico')

        # Entry Field
        entry= EntryField(self)
        image_original = Image.open(f'{self.script_directory}/Placeholder.png')

        entry_var = ctk.StringVar()
        entry = ctk.CTkEntry(
            self, placeholder_text="write some texts", textvariable=entry_var)
        entry.pack()
        button = ctk.CTkButton(self, text="CTkButton",
                               command=lambda: print(f'{entry_var.get()}'))
        button.pack()


app = App('QR Code generator', (400, 400))
app.mainloop()
