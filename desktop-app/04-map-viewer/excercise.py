import customtkinter as ctk
import os
import tkintermapview
from settings import *
from geopy.geocoders import Nominatim


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode('light')
        super().__init__()
        self.title('Map viewer')
        self.geometry("1200x800+10+50")
        self.iconbitmap(
            f"{os.path.dirname(os.path.realpath(__file__))}/map.ico")
        self.minsize(800, 600)

        # data
        self.input_string = ctk.StringVar()

        # event
        self.bind("<Return>", self.submit_location)
        # layout
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=8, uniform='a')

        # widget
        self.map = MapWidget(self, self.input_string)
        self.history = HistoryFrame(self)
        # item = HistoryItem(history, city="Paris", country="France")

    def submit_location(self, event):
        geolocator = Nominatim(user_agent='my-user')
        location = geolocator.geocode(self.input_string.get())
        city = str.split(location.address, ',')[0]
        country = str.split(location.address, ',')[-1]
        self.history.add_history(city=city, country=country)
        self.map.set_address(self.input_string.get())
        self.input_string.set(value='')

    def input_change(self, event, *args):
        self.map.set_address(self.input_string.get())
        self.input_string.set(value='')


class MapWidget(tkintermapview.TkinterMapView):
    def __init__(self, parent, input_string):
        super().__init__(parent)
        self.grid(row=0, column=1, sticky='nsew')

        # Entry
        LocationEntry(self, input_string)


class LocationEntry(ctk.CTkEntry):
    def __init__(self, parent, input_string):
        super().__init__(parent, textvariable=input_string)
        self.place(relx=0.5, rely=0.8, anchor="center")


class HistoryFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, ):
        super().__init__(parent, bg_color=SIDE_PANEL_BG)
        self.grid(row=0, column=0, sticky='nsew')

    def add_history(self, city, country):
        HistoryItem(self,  city, country)


class HistoryItem(ctk.CTkFrame):
    def __init__(self, parent, city, country):
        super().__init__(parent, fg_color='transparent')
        self.rowconfigure(0, weight=1, uniform='b')
        self.columnconfigure(0, weight=8, uniform='a')
        self.columnconfigure(1, weight=2, uniform='a')

        if city == country:
            button1_text = city
        else:
            button1_text = f"{city}, {country}"
        button1 = ctk.CTkButton(self, text=button1_text, command=self.remove, text_color=TEXT_COLOR,
                                fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR)
        button1.grid(row=0, column=0, sticky='nsew')

        button = ctk.CTkButton(self, text='x', command=self.remove, text_color=TEXT_COLOR,
                               fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR)
        button.grid(row=0, column=1, sticky='nsew')

        self.pack(side='top', fill='x', padx=0.5, pady=0.5)

    def remove(self):
        self.pack_forget()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
