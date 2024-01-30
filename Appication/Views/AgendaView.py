from tkinter import ttk
import tkinter as tk

from Appication.Views.Compononents import *
from Appication.Helper import *
from tkcalendar import Calendar


class AgendaView(ttk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent)

        self.cal = None
        self.root = parent
        self.data = data
        self.message_box = None

        self.header = self.header = Header(self, "calender.png", "calender", "dodgerblue", 25)

        self.build_layouts()

        self.build_message_box()



    def build_layouts(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        ttk.Style(self).configure("TFrame", background="whitesmoke")
        self.configure(style="TFrame", borderwidth=2, width=500, height=500)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

        self.cal = Calendar(self, selectmode="day", year=2024, month=1, day=1)

        self.cal.grid(row=1)

        button = ttk.Button(self, command=self.selectDate)
        button.grid(row=2)

    def selectDate(self):
        print(self.cal.get_date())

    def build_message_box(self):

        self.message_box = ttk.Frame(self)
        self.message_box.grid(row=1, column=0, sticky="nsew")
        self.message_box.columnconfigure(0, weight=17)
        self.message_box.columnconfigure(1, weight=8)
        self.message_box.columnconfigure(2, weight=1)
        self.message_box.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        label = tk.Label(self.message_box,
                         background="whitesmoke",
                         highlightthickness=1,
                         highlightbackground="#aaa")
        label.grid(row=0, column=0, sticky="nsew")


        label.rowconfigure(0, weight=1)
        label.rowconfigure(1, weight=1)
        label.rowconfigure(2, weight=1)
        label.rowconfigure(3, weight=1)
        label.columnconfigure(0, weight=1)



        self.calender_pic = generateIcon("calender.png", 21, 21)


        calender = tk.Button(label, text="click", image=self.calender_pic, relief="flat")
        calender.grid(row=0, column=0, sticky="nsew", pady=10)

        calender = tk.Button(label, text="click", image=self.calender_pic, relief="flat")
        calender.grid(row=1, column=0, sticky="nsew", pady=10)

        self.todo_pic = generateIcon("todo.png", 21, 22)
        calender = tk.Button(label, text="click", image=self.todo_pic, relief="flat")
        calender.grid(row=2, column=0, sticky="nsew", pady=10)

        calender = tk.Button(label, text="click", image=self.calender_pic, relief="flat")
        calender.grid(row=3, column=0, sticky="nsew", pady=10)

        canvas = tk.Canvas(self.message_box, background="whitesmoke")
        canvas.grid(row=0, column=1, sticky="nsew")
        canvas.grid_propagate(False)

        self.message_canvas = canvas

        scrollbar = tk.Scrollbar(self.message_box, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=2, sticky="nsew")

        frame = tk.Frame(self.message_box, bg="red")

        self.message_box = frame

        canvas.create_window((0, 0), window=self.message_box, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)



        canvas.bind("<Configure>", self.on_canvas_configure)

    def on_canvas_configure(self, event):
        self.message_canvas.configure(scrollregion=self.message_canvas.bbox("all"))
        self.message_canvas.update_idletasks()
        self.update_messages()
        print("scrolled")
