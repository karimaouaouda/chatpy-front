import tkinter

from PIL import Image, ImageTk


def is_valid_string(param):
    if not isinstance(param, str) or not param:
        return False
    else:
        return True


def is_valid_dict(param):
    if not isinstance(param, dict) or not param:
        return False
    else:
        return True


def is_valid_list(param):
    if not isinstance(param, list) or not param:
        return False
    else:
        return True

def generateIcon(icon, w, h):
    photo = Image.open(icon)
    photo = photo.resize((w, h), 2)

    pic = ImageTk.PhotoImage(photo)

    return pic


def make_grid(widget: tkinter.Widget, row_count: int, column_count: int):
    for i in range(column_count):
        widget.columnconfigure(i, weight=1)

    for i in range(row_count):
        widget.rowconfigure(i, weight=1)
