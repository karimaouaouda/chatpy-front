from tkinter import ttk
import tkinter as tk
from Appication.Helper import *


class Component(tk.Frame):
    def __init__(self, parent, bg, h):
        super().__init__(parent, background=bg, height=h)
        self.data = {}


class HeaderComponent(Component):
    def __init__(self, parent, icon, title, bg, h):
        super().__init__(parent, bg, h)

        self.icon = icon
        self.title = title
        self.img = None

        self.build_layouts()

        self.add_icon()

        self.add_title()

    def build_layouts(self):
        self.grid_propagate(False)  # for display
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.rowconfigure(0, weight=1)

        self.grid(column=0, row=0, sticky="nsew")  # nsew sticky arg is mean that this will take all the spacce

    def add_icon(self):
        label = tk.Label(self, background="white", height=200)
        label.grid(column=0, row=0, sticky="nsew")

        """start adding pic to label"""
        self.img = generateIcon(self.icon, 21, 22)

        label.configure(image=self.img)
        label.image = self.img

    def add_title(self):
        title = tk.Label(self, background="dodgerblue",
                         foreground="white",
                         text=self.title,
                         font=("cursive", 25),
                         anchor=tk.CENTER
                         )
        #

        title.grid(row=0, column=1, sticky="nsew")
