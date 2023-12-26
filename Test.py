from tkinter import ttk
import tkinter as tk


winWidth = 500
winHeight = 500

app = tk.Tk()

def resizing(event):
    if event.widget == app:
        if getattr(app, "_after_id", None):
            app.after_cancel(app._after_id)
        print(app.winfo_width())

app.bind("<Configure>", resizing)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

str1 = "{}x{}+{}+{}".format(winWidth, winHeight, int(( (screen_width - winWidth) / 2)), int(( (screen_height - winHeight) / 2)))


pane = ttk.PanedWindow(app, orient="vertical", width=winWidth, height=winHeight)

app.title("PySharm Chat")

app.geometry(str1)
app.minsize(winWidth, winHeight)

app.iconbitmap("chat.ico")

app.config(background='dodgerblue')

style = ttk.Style()
style.configure("TFrame", background='whitesmoke', highlightthickness=0, borderwidth=0)

frame = ttk.Frame(app, width=400, height=50, relief="flat", style='TFrame')

frame.grid_propagate(False)

label = ttk.Label(frame, text="some labe")

txt = 5

btn = ttk.Button(frame, text="click here")

formFrame = ttk.Frame(app, width=400, height=50, relief="flat", style='TFrame')

entry = ttk.Entry(formFrame, width=100, background='red')

formFrame.grid_propagate(False)


frame.pack()
formFrame.pack()
entry.grid(row=0, column=0)
pane.pack()
app.mainloop()


