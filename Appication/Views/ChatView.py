import threading
from tkinter import ttk
import tkinter as tk

import mouse
from PIL import ImageTk, Image
import pyaudio
import wave
import speech_recognition as sr
from threading import Thread
from Appication.Views.Components import *
from mouse import WheelEvent


class ChatView(ttk.Frame):
    def __init__(self, root, user):
        super().__init__(root)
        self.message_canvas = None
        self.speechText = tk.StringVar()
        self.formEntry = None
        self.img = None
        self.header = None
        self.user = user
        self.form = {}

        self.listenThread = Thread(target=self.listen, args=(), daemon=True)


        self.listening = False

        self.message_count = -1

        self.messages = []

        self.root = root

        self.build_layouts()

        self.build_header()

        self.build_message_box()

        self.build_form()

        self.message_box.bind("<Configure>", self.on_canvas_configure)

    def build_layouts(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=8)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        ttk.Style(self).configure("TFrame", background="whitesmoke")
        self.configure(style="TFrame", borderwidth=2, width=500, height=500)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

    def on_mouse_scroll(self):
        print(f"Scrolled {5} units")
    def build_header(self):
        """build the header for the conversation gui"""

        self.header = tk.Frame(self, background="dodgerblue")  # init the frame
        self.header.grid_propagate(False)  # for display


        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=5)
        self.header.rowconfigure(0, weight=1)

        self.header.grid(column=0, row=0, sticky="nsew")  # nsew sticky arg is mean that this will take all the spacce


        label = tk.Label(self.header, background="white")
        label.grid(column=0, row=0, sticky="nsew")

        """start adding pic to label"""
        photo = Image.open("chat.png")
        photo = photo.resize((21, 22), 2)

        img = ImageTk.PhotoImage(photo)
        self.img = img

        label.configure(image=img)
        label.image = img

        # """start adding the title to the interface"""
        titleLabel = tk.Label(self.header, background="green",
                              foreground="white",
                              text="hello there",
                              font=("cursive", 25),
                              anchor=tk.CENTER
                              )
        #

        titleLabel.grid(row=0, column=1, sticky="nsew")

        #
        # ttk.Style(self).configure("TFrame", background="red")
        #
        # self.configure(style="TFrame", borderwidth=2, width=500, height=500)
        #
        # img = Image.open("chat.png")
        # img = img.resize((50, 50), 2)
        #
        # img = ImageTk.PhotoImage(img)
        #
        # self.grid(row=0, column=0)
        #
        # self.heading = tk.Frame(self, background='black')
        #
        # label = tk.Label(self.heading, image=img, height=50)
        # self.heading.grid(row=0, column=0, columnspan=3, sticky="nsew")
        #
        # label.configure(image=img)
        # label.image = img
        #
        #
        #
        # self.grid_propagate(False)
        #
        #
        # left_panel = tk.Frame(self, background="green")
        #
        # left_panel.grid(row=1, column=0, sticky="nsew")
        #
        # message_box = tk.Frame(self, background="yellow")
        # message_box.grid(row=1, column=1, columnspan=2, sticky="nsew")
        #
        #
        # button = tk.Button(message_box, command=self.handleAudioClick)
        #
        #
        # form_box = tk.Frame(self, background='black')
        # form_box.grid(row=2, column=0, columnspan=3, sticky="nsew")
        #
        # recordingPanel = tk.Frame(self, width=200, height=100)
        # recordingPanel.grid(row=1, column=1)
        #
        # recordingPanel.rowconfigure(0, weight=1)
        # recordingPanel.rowconfigure(1, weight=1)
        #
        # recText = tk.Label(recordingPanel, text="recording...")
        # recText.grid(row=0, column=0, sticky=tk.W)
        #
        # recStopBtn = tk.Button(recordingPanel, text="stop recording")
        # recStopBtn.grid(row=1, column=0, sticky=tk.W)
        #
        # recordingPanel.grid_propagate(False)


    def handleAudioClick(self):
        if self.listening is True:
            self.listening = False
            print("stopped")
            self.show_text()
        else:
            self.listening = True
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
                print(text)
                self.speechText.set(text)
            except:
                print("no value found")
        return 1


    def testAction(self):
        self.message_count = self.message_count + 1
        message = MessageComponent(self.message_box, "loading {} messages".format(self.message_count))
        message.grid(row=self.message_count, column=0, sticky="ew", padx=10, pady=10)
        print("added...{}".format(self.message_count))

        self.messages.append(message)

        self.message_canvas.bind("<Configure>", self.on_canvas_configure)





    def build_form(self):
        form = tk.Frame(self, background="yellow")
        form.grid(row=2, column=0, sticky="nsew")

        form.rowconfigure(0, weight=1)
        form.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=4)
        form.columnconfigure(2, weight=1)

        mic = tk.Button(form, text="Send",
                        background="green",
                        foreground="white",
                        relief="flat",
                        image=self.img,
                        command=self.handleAudioClick
                        )
        mic.grid(row=0, column=0)


        entry = tk.Entry(form, background="yellow", textvariable=self.speechText)
        entry.grid(row=0, column=1)

        self.formEntry = entry


        btn = tk.Button(form, text="Send", background="green", command=self.testAction, foreground="white", relief="flat", image=self.img)
        btn.grid(row=0, column=2)

    def build_message_box(self):

        self.message_box = ttk.Frame(self)
        self.message_box.grid(row=1, column=0, sticky="nsew")
        self.message_box.columnconfigure(0, weight=4)
        self.message_box.columnconfigure(1, weight=8)
        self.message_box.columnconfigure(2, weight=1)
        self.message_box.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        label = tk.Label(self.message_box, background="green")
        label.grid(row=0, column=0, sticky="nsew")

        canvas = tk.Canvas(self.message_box, background="yellow")
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