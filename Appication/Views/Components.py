from tkinter import ttk
import tkinter as tk
from abc import ABC, abstractmethod


class Component(tk.Label):
    def __init__(self, parent, t):
        super().__init__(parent)
        self.data = {}


class MessageComponent(Component):
    def __init__(self, parent, t):
        super().__init__(parent, t)
        self.data["message"] = "loading..."

        def button_click(self):
            print("clickde me")

        l = tk.Label(self, wraplength=400,text=" some text here i don't know what in this text but i love you bro dqsdqsdqsdsqd"
                                "sfdfsdfsfdsfsdfsd")

        l.pack()

        button = tk.Button(self, text="Click Me", command=button_click)
        button.pack(pady=5)

    def message(self, message):
        self.data["message"] = message