from Appication.Views.LoginView import LoginView
from Appication.Views.ChatView import ChatView
from Appication.Views.AgendaView import AgendaView

# from Appication.Views.WelcomeView import WelcomeView

views = {
    # "welcome": WelcomeView,
    "login": LoginView,
    "chat": ChatView,
    "agenda": AgendaView,
}


class ViewBuilder:
    def __init__(self, view_key):

        if view_key not in views:
            raise ValueError('Invalid View name')

        self.__view_key = view_key
        self.__data = {}

    def appendData(self, data=None):
        if data is None:
            self.__data = {}
        else:
            self.__data = data

    def build(self, master):
        return views[self.__view_key](master, self.__data)
