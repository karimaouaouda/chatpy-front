import tkinter as tk
import random
from gtts import gTTS
import pyttsx3
from playsound import playsound
from PIL import ImageTk, Image




class Component(tk.Label):
    def __init__(self, parent, t):
        super().__init__(parent)
        self.data = {}


def text_to_speech_gTTS(text, lang='en', save_to_file="temp.mp3"):
    tts = gTTS(text=text, lang="en", slow=False)

    tts.save("temp.mp3")
    playsound("temp.mp3")


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text, "karim voice")
    engine.runAndWait()


class MessageComponent(Component):
    def __init__(self, parent, t):
        super().__init__(parent, t)



        self.data["message"] = tk.StringVar(value=t)

        l = tk.Label(self, wraplength=400, textvariable=self.data["message"])

        l.pack()

        photo = Image.open("chat.png")
        photo = photo.resize((5, 5), 2)

        img = ImageTk.PhotoImage(photo)

        button = tk.Button(self, text="Click Me", command=self.button_click )
        button.pack(pady=5)

    def message(self, message):
        self.data["message"] = message

    def updateText(self, message):
        self.data["message"].set(message)

    def button_click(self, event = None):
        text_to_speech_gTTS(self.data["message"].get())
