import tkinter as tk
from tkinter import ttk
from Appication.Helper import *


class MenuBuilder:
    def __init__(self):
        self.menu = {}


    def create(self, menu_name):
        if not is_valid_string(menu_name):
            raise ValueError("string must be provided as a menu name, you provide {}".format(type(menu_name)))

        if menu_name not in self.menu:
            self.menu[menu_name] = {}

        return self

    def appendOptions(self, name, options):
        if not is_valid_list(options):
            raise ValueError("dictionary must be provided as a menu options, you provide {}".format(type(options)))

        self.create(menu_name=name)

        self.menu[name] = options

    def build(self, master):
        menu = tk.Menu(master)
        master.config(menu=menu)


        for menu_name, options in self.menu.items():
            sub_menu = tk.Menu(menu, tearoff=0)
            menu.add_cascade(label=menu_name, menu=sub_menu)

            for index, option in enumerate(options):
                # Add options to the File menu
                sub_menu.add_command(label=option['label'], command=option['action'])

                if index < len(options) - 1:
                    sub_menu.add_separator()


        return menu
