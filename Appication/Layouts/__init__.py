from tkinter import ttk
import tkinter as tk
from Appication.Builders.MenuBuilder import MenuBuilder
from Appication.Views.Compononents import *
from Appication.Helper import *


class AppLayout(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, borderwidth=10, border=10, background='red')



        self.menu = self.build_menu(master)

        self.build_layouts()



        self.header = Header(self, "chat.png", "layout", "dodgerblue", 10)




    def action(self, string):
        print(f"clicked menu {string}")

    def build_layouts(self):
        self.rowconfigure(1, weight=1)
        self.rowconfigure(1, weight=4)

        self.grid_propagate(False)
    def build_menu(self, master):
        builder = MenuBuilder()

        options = [
            {
                "label": "open",
                "action": lambda: self.action("open")
            },
            {
                "label": "save",
                "action": lambda: self.action("save")
            }
        ]

        builder.create("file").appendOptions("file", options)


        return builder.build(master)

