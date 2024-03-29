from typing import Optional, Tuple, Union
import customtkinter as ctk
import math


class Mesures(ctk.CTkFrame):
    PADX = 8

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.place(relx=0, rely=0.5, relwidth=1, relheight=0.5, anchor="nw")
        self.rowconfigure((0, 1), weight=1, uniform="a")
        self.columnconfigure(0, weight=1)

        # set heigh
        self.heigh_value = ctk.DoubleVar()
        self.heigh_frame = ctk.CTkFrame(self, fg_color="white", height=80)
        self.heigh_frame.grid(row=1, column=0, sticky="we", padx=self.PADX)
        self.tall_slider = ctk.CTkSlider(
            self.heigh_frame,
            from_=0.1,
            to=3,
            command=self.slider_event, variable=self.heigh_value
        )
        self.tall_slider.pack(side="left", expand=True)
        label_heigh = ctk.CTkLabel(
            self.heigh_frame, text="label", textvariable=self.heigh_value, width=20
        )
        label_heigh.pack(side="right")
        # set weight

        self.weight_frame = ctk.CTkFrame(self, fg_color="white", height=70)
        self.weight_frame.grid(row=0, column=0, sticky="we", padx=self.PADX)
        less_button1 = ctk.CTkButton(
            self.weight_frame, width=50, height=50, text="-", command=lambda: self.change_weight('less'))
        less_button2 = ctk.CTkButton(
            self.weight_frame, width=30, height=30, text="-", command=lambda: self.change_weight('lessx'))
        less_button1.pack(side="left", expand=True, fill="x", padx=10)
        less_button2.pack(side="left", expand=True, fill="x", padx=10)
        self.label_weight = ctk.CTkLabel(self.weight_frame,
                                         text=0)
        self.label_weight.pack(side="left", expand=True)
        plus_button = ctk.CTkButton(
            self.weight_frame, width=50, height=50, text="+", command=lambda: self.change_weight('plus'))
        plus_button.pack(side="left", expand=True)

    def slider_event(self, value):
        self.tall_slider.set(round(value, 2))

    def change_weight(self, operation, *agrs):
        if operation == 'less':
            self.label_weight.configure(text=round(
                float(self.label_weight._text) - 0.1, 1))
        elif operation == 'plus':
            self.label_weight.configure(text=round(
                float(self.label_weight._text) + 0.1, 1))
        else:
            raise ValueError()

    def get_bmi_value(self):
        return round(float(self.label_weight._text)/self.heigh_value**2, 1)


class BMIValue(ctk.CTkFrame):

    def __init__(self, parent, value):
        super().__init__(parent, fg_color="transparent", )
        self.place(relx=0.5, rely=0.5, relwidth=1,
                   relheight=1, anchor="center")
        label = ctk.CTkLabel(self, font=(None, 80),
                             text_color="white", text=value)
        label.place(relx=0.5, rely=0.5, anchor="center")


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#59C2AE")
        # window
        self.title("")
        self.geometry("400x400")
        self.minsize(400, 400)
        self.wm_attributes("-toolwindow", "True")  # Remove icon window
        # layout
        self.rowconfigure((0, 1), weight=1, uniform="a")
        self.columnconfigure(0, weight=1)

        # widgets
        bmi_value_var = ctk.DoubleVar(value=0)
        bmi = BMIValue(self, bmi_value_var.get())
        bmi.grid(row=0, column=0, sticky="nswe")
        bmi.place()

        mesure = Mesures(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
