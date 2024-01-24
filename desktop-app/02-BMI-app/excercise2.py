from typing import Optional, Tuple, Union
import customtkinter as ctk
from settings import *


class ResultText(ctk.CTkLabel):
    def __init__(self, parent, bmi_string):
        super().__init__(parent)
        label = ctk.CTkLabel(parent, text=80, font=(
            FONT, MAIN_TEXT_SIZE), textvariable=bmi_string)
        label.grid(row=0, column=0, rowspan=2)


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent, weight_float):
        super().__init__(parent, bg_color='transparent',
                         fg_color=WHITE, corner_radius=CORNER_RADIUS)
        self.weight_float = weight_float
        self.grid(row=2, column=0, sticky='nsew', padx=PADX, pady=15)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2, uniform="b")
        self.columnconfigure(1, weight=1, uniform="b")
        self.columnconfigure(2, weight=3, uniform="b")
        self.columnconfigure(3, weight=1, uniform="b")
        self.columnconfigure(4, weight=2, uniform="b")
        # variable
        self.output_string = ctk.StringVar()

        # widget
        minus_button = ctk.CTkButton(
            self,
            text='-',
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            text_color=BLACK,
            command=lambda: self.update_weight(('minus', 'large'))
        )
        minus_button.grid(row=0, column=0, sticky='nsew', padx=PADX, pady=PADX)

        minus_button_small = ctk.CTkButton(
            self,
            text='-',
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            text_color=BLACK,
            command=lambda: self.update_weight(('minus', 'small'))
        )
        minus_button_small.grid(row=0, column=1, sticky='nsew', pady=PADX+10)

        large_button = ctk.CTkButton(
            self,
            text='+',
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            text_color=BLACK,
            command=lambda: self.update_weight(('plus', 'large'))
        )
        large_button.grid(row=0, column=4, sticky='nsew', padx=PADX, pady=PADX)
        large_button_small = ctk.CTkButton(
            self,
            text='+',
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            text_color=BLACK,
            command=lambda: self.update_weight(('plus', 'small'))
        )
        large_button_small.grid(row=0, column=3, sticky='nsew', pady=PADX+10)

        weight_label = ctk.CTkLabel(
            self,
            text_color=BLACK,
            textvariable=self.output_string,
            font=(FONT, INPUT_FONT_SIZE)
        )
        weight_label.grid(row=0, column=2)

    def update_weight(self, info=None):

        if info[0] == 'plus':
            if info[1] == 'large':
                self.weight_float.set(self.weight_float.get() + 1)
            else:
                self.weight_float.set(self.weight_float.get() + 0.1)
        else:
            if info[1] == 'large':
                self.weight_float.set(self.weight_float.get() - 1)
            else:
                self.weight_float.set(self.weight_float.get() - 0.1)
        if self.weight_float.get() < 0:
            self.weight_float.set(0)
        self.output_string.set(f'{round(self.weight_float.get(),1)}kg')


class HeighInput(ctk.CTkFrame):
    def __init__(self, parent, heigh_int):
        super().__init__(parent, bg_color='transparent',
                         fg_color=WHITE, corner_radius=CORNER_RADIUS)
        self.grid(row=3, column=0, sticky='nsew', padx=PADX, pady=10)
        slider = ctk.CTkSlider(self,
                               from_=100,
                               to=250,
                               command=self.update_output_text,
                               button_color=GREEN,
                               button_hover_color=GRAY,
                               progress_color=GREEN,
                               fg_color=LIGHT_GRAY,
                               variable=heigh_int
                               )
        slider.pack(side='left', fill='x', expand=True, padx=10)

        self.output_text = ctk.CTkLabel(
            self, text='1.5m', text_color=BLACK, font=(FONT, INPUT_FONT_SIZE))
        self.output_text.pack(side='left', expand=True,
                              )

    def update_output_text(self, value):
        self.output_text.configure(text=f'{round(value/100,1)}m')


class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(parent)


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#59C2AE")
        # window
        self.title("")
        self.geometry("400x400")
        self.minsize(400, 400)
        self.resizable(False, False)
        # self.wm_attributes("-toolwindow", "True")  # Remove icon window
        # layout
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.columnconfigure(0, weight=1)
        # variable
        self.heigh_int = ctk.IntVar(value=100)
        self.weight_float = ctk.DoubleVar()
        self.bmi_string = ctk.StringVar()

        # event
        self.heigh_int.trace_add('write', self.update_bmi)
        self.weight_float.trace_add('write', self.update_bmi)
        # widgets
        WeightInput(self, self.weight_float)
        HeighInput(self, self.heigh_int)
        ResultText(self, self.bmi_string)
        UnitSwitcher(self)

    def update_bmi(self, *args):
        if self.heigh_int.get() != 0:
            heigh_meter = self.heigh_int.get()/100
            weight_kg = self.weight_float.get()
            bmi = round(weight_kg/heigh_meter**2, 2)
            self.bmi_string.set(bmi)


if __name__ == "__main__":
    app = App()
    app.mainloop()
