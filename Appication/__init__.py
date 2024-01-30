import tkinter as tk
from Appication.Views.LoginView import LoginView
from Appication.Views.ChatView import ChatView
import Appication.Controllers.AuthController as AuthController

def generateIcon(icon, w, h):
    photo = Image.open(icon)
    photo = photo.resize((w, h), 2)

    pic = ImageTk.PhotoImage(photo)

    return pic

def config(key):
    configs = {
        "window_width" : 500,
        "window_height" : 500,
        "title" : "ChatPy"
    }

    if key not in configs:
        raise Exception("Invalid key")

    return configs[key]


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.s = True
        self.user = None
        self.isAuthenticated = False

        self.views = {
            "login": LoginView,
            "chat": ChatView,
            # "agenda": AgendaView
        }

        self.width = config("window_width")
        self.height = config("window_height")

        self.title(config("title"))

        self.initWindow()

        self.currentFrame = None

        self.renderView("chat")

    def initWindow(self):
        # first we wil set the window width,height and place it at the center
        self.size = (config("window_width"), config("window_height"))
        # after that we will cet an icon to our program
        self.iconbitmap('chat.ico')


    def renderView(self, view):
        self.render(view, self)

    def loginAction(self, event):
        self.render(ChatView, self)

    def render(self, view, root, data=None):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
            self.currentFrame = None

        self.currentFrame = self.views[view](root, data)



