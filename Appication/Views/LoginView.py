from tkinter import ttk
import tkinter as tk


class LoginView(ttk.Frame):
    def __init__(self, root, data):
        super().__init__(root)
        style = ttk.Style(self)
        style.configure('TFrame')
        self.heading = tk.Label(self, text="Login now!",
                                 fg="red",
                                 font=("Helvetica", 25),
                                 padx=5,
                                 pady= 10
                                 )

        self.inputs = ttk.Frame(self, width=450, height=350, style='TFrame')

        style = ttk.Style()
        style.configure('TEntry', width=12)

        ttk.Label(self.inputs, text="Enter email:", font=("Helvetica", 15)).place(x=0, y=10)
        self.email_entry = ttk.Entry(self.inputs, font=("Helvetica", 15), style="TEntry")
        self.email_entry.place(x=10, y=45)

        self.statusLabel = tk.Label(self.inputs, font=("Helvetica", 10), text="ds")
        self.statusLabel.place(x=50, y=250)

        ttk.Label(self.inputs, text="Enter email:", font=("Helvetica", 15)).place(x=0, y=80)
        self.password_entry = ttk.Entry(self.inputs, font=("Helvetica", 15), style='TEntry')
        self.password_entry.place(x=10, y=115)

        self.login_btn = ttk.Button(self.inputs, text="Login")
        self.login_btn.place(x=10, y=150)


        self.pack()
        self.heading.pack()
        self.inputs.pack()

    def bindAction(self, action):
        if action is not None:
            self.login_btn.bind("<Button-1>", action)

    def values(self):
        return {
            "email": self.email_entry.get(),
            "password": self.password_entry.get()
        }


    def error(self, error):
        self.statusLabel['text'] = "error"
        self.statusLabel['fg'] = "red"