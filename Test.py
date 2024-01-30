import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Open File")
    if file_path:
        print(f"Opened file: {file_path}")

def exit_application():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Personalized Menu Example")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add options to the File menu
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_application)

# Start the Tkinter event loop
root.mainloop()


def __init__(self):
    super().__init__()
    self.s = True
    self.user = None
    self.isAuthenticated = False

    self.views = {
        "login": LoginView,
        "chat": ChatView,
        "agenda": AgendaView
    }

    self.width = config("window_width")
    self.height = config("window_height")

    self.title(config("title"))

    self.initWindow()

    self.currentFrame = None

    self.renderView("agenda")


def initWindow(self):
    # first we wil set the window width,height and place it at the center
    self.size = (config("window_width"), config("window_height"))
    # after that we will cet an icon to our program
    self.iconbitmap('chat.ico')


def renderView(self, view):
    self.render(view, self)


def loginAction(self, event):
    self.render(ChatView, self)


def loginAction2(self, event):
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

    self.currentFrame = self.views[view](root, data)



