import asyncio
import json.decoder
from tkinter import ttk
import tkinter as tk

import pyaudio
import wave
import speech_recognition as sr
from threading import Thread

from Appication.Views.Compononents import *
from Appication.Helper import *

import Appication.Controllers.MessagingController as MessageController


def send_message(message=None):
    if message is not None:
        return MessageController.send(message)


def send_msg(component, msg):
    response = send_message(message=msg)
    print(response)
    msg = json.loads(response.content.decode())['content']

    component.updateText(message=msg)


class ChatView(ttk.Frame):
    def __init__(self, root, user):
        super().__init__(root)
        self.tools = None
        self.chat_ico = None
        self.todo_pic = None
        self.calender_pic = None
        self.listenThread = None
        self.message_canvas = None
        self.entryText = tk.StringVar()
        self.formEntry = None
        self.img = None
        self.header = None
        self.user = user
        self.form = {}
        self.listening = False

        self.message_count = -1

        self.messages = []

        self.mic_pic = None

        self.root = root

        self.build_layouts()

        # self.header = Header(self, "chat.png", "chatpy", "dodgerblue", 25)
        self.header = makeComponent("header", self, icon="chat.png", title="chatpy", bg="dodgerblue", h=25)

        self.build_message_box()

        self.build_form()

        self.message_box.bind("<Configure>", self.on_canvas_configure)

    """build functions here"""

    def build_layouts(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        ttk.Style(self).configure("TFrame", background="whitesmoke")
        self.configure(style="TFrame", borderwidth=2, width=500, height=500)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

    def build_form(self):
        form = tk.Frame(self, background="whitesmoke")
        form.grid(row=2, column=0, sticky="nsew")

        form.rowconfigure(0, weight=1)
        form.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=4)
        form.columnconfigure(2, weight=1)

        self.mic_pic = generateIcon("mic.png", 21, 22)

        mic = tk.Button(form, text="Send",
                        background="whitesmoke",
                        foreground="green",
                        relief="flat",
                        image=self.mic_pic,
                        command=self.handleAudioClick
                        )
        mic.grid(row=0, column=0)

        entry = tk.Entry(form, background="white",
                         textvariable=self.entryText,
                         font=("Arial", 12),
                         borderwidth=10,
                         relief="flat",
                         foreground="dodgerblue",
                         highlightcolor="dodgerblue",
                         highlightthickness=1,
                         highlightbackground="#aaa"
                         )
        entry.grid(row=0, column=1, sticky="ew", pady=5)

        self.formEntry = entry

        self.img = generateIcon("send.png", 21, 22)

        btn = tk.Button(form, text="Send",
                        background="whitesmoke",
                        command=self.testAction,
                        foreground="white",
                        relief="flat",
                        image=self.img
                        )
        btn.grid(row=0, column=2)

    def build_message_box(self):

        self.message_box = ttk.Frame(self)
        self.message_box.grid(row=1, column=0, sticky="nsew")
        self.message_box.columnconfigure(0, weight=17)
        self.message_box.columnconfigure(1, weight=8)
        self.message_box.columnconfigure(2, weight=1)
        self.message_box.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.tools = makeComponent("left_bar", self.message_box, data=None)

        canvas = tk.Canvas(self.message_box, background="whitesmoke")
        canvas.grid(row=0, column=1, sticky="nsew")
        canvas.grid_propagate(False)

        self.message_canvas = canvas

        scrollbar = tk.Scrollbar(self.message_box, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=2, sticky="nsew")

        frame = tk.Frame(self.message_box)

        self.message_box = frame

        canvas.create_window((0, 0), window=self.message_box, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.bind("<Configure>", self.on_canvas_configure)

    """other functions here"""

    def on_mouse_scroll(self):
        print(f"Scrolled {5} units")

    def handleAudioClick(self):
        if self.listening is True:
            self.listening = False
            print("stopped")
            self.show_text()
        else:
            self.listening = True
            if self.listenThread is not None and self.listenThread.is_alive():
                self.listenThread.join()

            self.listenThread = Thread(target=self.listen, args=(), daemon=True)
            self.listenThread.start()

        return True

    def show_text(self):
        r = sr.Recognizer()

        with sr.AudioFile("output.wav") as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            try:
                text = r.recognize_google(audio_data)
                self.entryText.set(text)
            except:
                print("no value found")
        return 1

    def testAction(self):
        # first let's push the message to the view
        self.message_count = self.message_count + 1
        message = makeComponent("message", self.message_box, message=self.formEntry.get())
        message.config(bg="blue", borderwidth=5)
        message.grid(row=self.message_count, column=1, sticky="w")

        # send the message to server and waiting for a response

        message = makeComponent("message", self.message_box, message="waiting...")
        message.config(bg="white", borderwidth=5)
        self.message_count = self.message_count + 1
        message.grid(row=self.message_count, column=1, sticky="w")

        #send the request
        #self.send_and_replace(messageComponent=message)

        send_msg(message, self.formEntry.get())



        # thread = Thread(target=send_msg, args=(message, "some input"))
        # thread.start()
        # thread.join()

        self.message_canvas.bind("<Configure>", self.on_canvas_configure)

    def on_canvas_configure(self, event):
        self.message_canvas.configure(scrollregion=self.message_canvas.bbox("all"))
        self.message_canvas.update_idletasks()
        print("scrolled")

    def update_messages(self):
        for message in self.messages:
            message.update()

    def startListen(self):
        self.listenThread.start()
        print("gone")

    def listen(self):
        print("listen...")
        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 2
        fs = 44100  # Record at 44100 samples per second
        seconds = 3
        filename = "output.wav"
        p = pyaudio.PyAudio()
        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        while self.listening:
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        print("finished listening")
