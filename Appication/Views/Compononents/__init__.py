from Appication.Views.Compononents import MessageComponent
from Appication.Views.Compononents import HeaderComponont
from Appication.Views.Compononents.HeaderComponont import HeaderComponent
from Appication.Views.Compononents.BarComponent import BarComponent


def Header(parent, kwargs):
    return HeaderComponent(parent, kwargs['icon'], kwargs['title'], kwargs['bg'], kwargs['h'])


def Message(parent, kwargs):
    return MessageComponent.MessageComponent(parent, kwargs['message'])


def LeftBar(parent, kwargs):
    return BarComponent(parent)



components = {
    "message": Message,
    "header": Header,
    "left_bar": LeftBar,

}


def makeComponent(key, master, **kwargs):
    return components[key](master, kwargs)
