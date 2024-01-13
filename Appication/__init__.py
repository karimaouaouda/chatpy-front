import tkinter as tk
from Appication.Views.LoginView import LoginView
from Appication.Views.ChatView import ChatView
import Appication.Controllers.AuthController as AuthController

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

        self.width = config("window_width")
        self.height = config("window_height")

        self.title(config("title"))

        self.initWindow()

        self.currentFrame = None

        self.render(ChatView, self)

        #self.currentFrame.bindAction(self.loginAction)

    def initWindow(self):
        # first we wil set the window width,height and place it at the center
        self.size = (config("window_width"), config("window_height"))
        # after that we will cet an icon to our program
        self.iconbitmap('chat.ico')

    def loginAction(self, event):
        response = AuthController.AuthController().login(self.currentFrame.values())
        print(response)
        if not response:
            self.currentFrame.error("some error was occurred, retry")

        else:
            if response['status']:
                self.user = response['user']
                self.isAuthenticated = True
                self.render(ChatView, self, self.user)
            else:
                self.currentFrame.error(response['message'])

    def render(self, view, root, data=None):
        if self.currentFrame is not None:
            self.currentFrame.destroy()
            self.currentFrame = None

        self.currentFrame = view(root, data)



