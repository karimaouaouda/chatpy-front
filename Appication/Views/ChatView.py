from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image


class ChatView(ttk.Frame):
    def __init__(self, root, user):
        super().__init__(root)
        self.user = user
        self.listening = False

        self.root = root

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=1)

        ttk.Style(self).configure("TFrame", background="red")

        self.configure(style="TFrame", borderwidth=2, width=500, height=500)

        img = Image.open("chat.png")
        img = img.resize((50, 50), 2)

        img = ImageTk.PhotoImage(img)

        self.grid(row=0, column=0)

        self.heading = tk.Frame(self, background='black')

        label = tk.Label(self.heading, image=img, height=50)
        self.heading.grid(row=0, column=0, columnspan=3, sticky="nsew")

        label.configure(image=img)
        label.image = img



        self.grid_propagate(False)


        left_panel = tk.Frame(self, background="green")

        left_panel.grid(row=1, column=0, sticky="nsew")

        message_box = tk.Frame(self, background="yellow")
        message_box.grid(row=1, column=1, columnspan=2, sticky="nsew")


        button = tk.Button(message_box, command=self.handleAudioClick)


        form_box = tk.Frame(self, background='black')
        form_box.grid(row=2, column=0, columnspan=3, sticky="nsew")

        recordingPanel = tk.Frame(self, width=200, height=100)
        recordingPanel.grid(row=1, column=1)

        recordingPanel.rowconfigure(0, weight=1)
        recordingPanel.rowconfigure(1, weight=1)

        recText = tk.Label(recordingPanel, text="recording...")
        recText.grid(row=0, column=0, sticky=tk.W)

        recStopBtn = tk.Button(recordingPanel, text="stop recording")
        recStopBtn.grid(row=1, column=0, sticky=tk.W)

        recordingPanel.grid_propagate(False)

    def handleAudioClick(self, event):
        if self.listening is True:
            self.listening = False