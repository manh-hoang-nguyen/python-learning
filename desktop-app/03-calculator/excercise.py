import customtkinter as ctk
import tkinter as tk
from settings import *
import darkdetect
import os
from PIL import Image, ImageTk

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class Calculator(ctk.CTk):
    def __init__(self):
        # setup
        self.is_dark = darkdetect.isDark()
        ctk.set_appearance_mode(f'{"dark" if self.is_dark else "light"}')
        super().__init__(fg_color=(WHITE, BLACK))
        self.title("")
        self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}")
        self.resizable(False, False)
        self.iconbitmap(f"{os.path.dirname(os.path.realpath(__file__))}/empty.ico")
        self.title_bar_color()

        # layout
        self.rowconfigure(tuple(range(MAIN_ROWS)), weight=1, uniform="a")
        self.columnconfigure(tuple(range(MAIN_COLUMNS)), weight=1, uniform="b")

        # data
        self.result_string = ctk.StringVar(value="0")
        self.formula_string = ctk.StringVar(value="")

        # widget

        self.create_widgets()

    def operator(self, operator):
        if operator == "clear":
            print("clear")
            self.result_string.set("0")
            self.formula_string.set("")
        elif operator == "percent":
            print("percent")
        elif operator == "invert":
            print("invert")
        else:
            raise ValueError()

    def update_result(self, character):
        print(character)
        self.result_string.set(self.result_string.get() + character)

    def create_widgets(self):
        # fonts
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)
        OutputLabel(self, 0, "se", main_font, self.formula_string)
        OutputLabel(self, 1, "e", result_font, self.result_string)

        # AC button
        Button(
            self,
            text="AC",
            row=OPERATORS["clear"]["row"],
            col=OPERATORS["clear"]["col"],
            font=main_font,
            func=lambda: self.operator("clear"),
            fg_color=COLORS["dark-gray"]["fg"],
            hover_color=COLORS["dark-gray"]["hover"],
            text_color=COLORS["dark-gray"]["text"],
        )
        # percentage button
        Button(
            self,
            text="%",
            row=OPERATORS["percent"]["row"],
            col=OPERATORS["percent"]["col"],
            font=main_font,
            func=lambda: self.operator("percent"),
            fg_color=COLORS["dark-gray"]["fg"],
            hover_color=COLORS["dark-gray"]["hover"],
            text_color=COLORS["dark-gray"]["text"],
        )
        # invert button
        raw_image = Image.open(
            f"{os.path.dirname(os.path.realpath(__file__))}/invert_light.png"
        )
        tk_image = ctk.CTkImage(raw_image.resize((25, 25)))

        ImageButton(
            self,
            image=tk_image,
            row=OPERATORS["invert"]["row"],
            col=OPERATORS["invert"]["col"],
            func=lambda: self.operator("invert"),
            fg_color=COLORS["dark-gray"]["fg"],
            hover_color=COLORS["dark-gray"]["hover"],
            text_color=COLORS["dark-gray"]["text"],
        )
        # button number
        for key, value in NUM_POSITIONS.items():
            print(key)
            button = ctk.CTkButton(
                self,
                text=key,
                font=main_font,
                text_color=BLACK,
                fg_color=COLORS.get("light-gray").get("fg"),
                hover_color=COLORS.get("light-gray").get("hover"),
                corner_radius=0,
                command=lambda: self.update_result(key),
            )
            button.grid(
                row=value.get("row"),
                column=value.get("col"),
                columnspan=value.get("span"),
                sticky="nsew",
                padx=STYLING["gap"],
                pady=STYLING["gap"],
            )
        # math button
        for key, value in MATH_POSITIONS.items():
            button = ctk.CTkButton(
                self,
                text=key,
                font=main_font,
                text_color=WHITE,
                fg_color=COLORS.get("orange").get("fg"),
                hover_color=COLORS.get("orange").get("hover"),
                corner_radius=0,
                command=self.update_formula,
            )
            button.grid(
                row=value.get("row"),
                column=value.get("col"),
                columnspan=value.get("span"),
                sticky="nsew",
                padx=STYLING["gap"],
                pady=STYLING["gap"],
            )

    def update_formula(self):
        pass

    def title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.info_id())
            DWMA_ATTRIBUTE = 35
            COLOR = (
                TITLE_BAR_HEX_COLORS["dark"]
                if self.is_dark
                else TITLE_BAR_HEX_COLORS["light"]
            )
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, DWMA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int)
            )
        except:
            pass


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(parent, text="123", font=font, textvariable=string_var)
        self.grid(row=row, column=0, columnspan=4, sticky=anchor)


class Button(ctk.CTkButton):
    def __init__(
        self, parent, text, row, col, font, func, fg_color, hover_color, text_color
    ):
        super().__init__(
            parent,
            font=font,
            command=func,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            text=text,
            corner_radius=0,
        )
        self.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=STYLING["gap"],
            pady=STYLING["gap"],
        )


class ImageButton(ctk.CTkButton):
    def __init__(
        self, parent, image, row, col, func, fg_color, hover_color, text_color
    ):
        super().__init__(
            parent,
            command=func,
            image=image,
            text="",
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            corner_radius=0,
        )
        self.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=STYLING["gap"],
            pady=STYLING["gap"],
        )


if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
