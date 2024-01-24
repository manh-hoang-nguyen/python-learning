import customtkinter as ctk
from settings import *
import darkdetect
import os
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
        self.title('')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)
        self.iconbitmap(
            f'{os.path.dirname(os.path.realpath(__file__))}/empty.ico')
        self.title_bar_color()

        # layout
        self.rowconfigure(tuple(range(MAIN_ROWS)), weight=1, uniform='a')
        self.columnconfigure(tuple(range(MAIN_COLUMNS)), weight=1, uniform='b')

        # data
        self.result_string = ctk.StringVar(value='0')
        self.formula_string = ctk.StringVar(value='')

        # widget

        self.create_widgets()

    def create_widgets(self):
        # fonts
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)
        OutputLabel(self, 0, 'se', main_font, self.formula_string)
        OutputLabel(self, 1, 'e', result_font, self.result_string)

        # button number

        for key, value in NUM_POSITIONS.items():
            button = ctk.CTkButton(self,
                                   text=key,
                                   font=main_font,
                                   text_color=BLACK,
                                   fg_color=COLORS.get('light-gray').get('fg'),
                                   corner_radius=0,
                                   command=self.update_formula
                                   )
            button.grid(
                row=value.get('row'),
                column=value.get('col'),
                columnspan=value.get('span'),
                sticky='nsew',

            )

    def update_formula(self):
        pass

    def title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.info_id())
            DWMA_ATTRIBUTE = 35
            COLOR = TITLE_BAR_HEX_COLORS['dark'] if self.is_dark else TITLE_BAR_HEX_COLORS['light']
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, DWMA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(parent, text='123', font=font, textvariable=string_var)
        self.grid(row=row, column=0, columnspan=4, sticky=anchor)


if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()
