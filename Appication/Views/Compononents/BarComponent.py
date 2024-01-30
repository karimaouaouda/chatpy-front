
import tkinter as tk

from Appication.Helper import generateIcon


class BarComponent(tk.Label):
    def __init__(self, master):
        super().__init__(master,
                         background="whitesmoke",
                         highlightthickness=1,
                         highlightbackground="#aaa")

        self.grid(row=0, column=0, sticky="nsew")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)

        self.calender_pic = generateIcon("calender.png", 21, 21)
        self.chat_ico = generateIcon("chat.png", 25, 25)

        calender = tk.Button(self, image=self.chat_ico, relief="flat")

        calender.grid(row=0, column=0, sticky="nsew", pady=10)

        calender = tk.Button(self, text="click", image=self.calender_pic, relief="flat")
        calender.grid(row=1, column=0, sticky="nsew", pady=10)

        self.todo_pic = generateIcon("todo.png", 21, 22)

        calender = tk.Button(self, text="click", image=self.todo_pic, relief="flat")
        calender.grid(row=2, column=0, sticky="nsew", pady=10)

        calender = tk.Button(self, text="click", image=self.calender_pic, relief="flat")
        calender.grid(row=3, column=0, sticky="nsew", pady=10)