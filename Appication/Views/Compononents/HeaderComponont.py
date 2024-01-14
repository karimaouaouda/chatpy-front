from tkinter import ttk
import tkinter as tk


class Component(tk.Label):
    def __init__(self, parent, t):
        super().__init__(parent)
        self.data = {}