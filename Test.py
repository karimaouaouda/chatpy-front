import tkinter as tk


def add_frame(content, color):
    global frame_counter
    new_frame = tk.Frame(canvas_frame, bg=color, padx=5, pady=5)
    new_frame.pack(side="top", fill="x")

    label = tk.Label(new_frame, text=content)
    label.pack(padx=5, pady=5)

    # Increase the row counter for the next frame

    frame_counter += 1


root = tk.Tk()

canvas = tk.Canvas(root, bg="lightblue")
canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

# Create a frame to hold the canvas
canvas_frame = tk.Frame(canvas, bg="lightblue")
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

# Counter for keeping track of rows
frame_counter = 0

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

add_frame("Frame 1 Content", "lightgreen")
add_frame("Frame 2 Content", "lightcoral")
add_frame("Frame 3 Content", "lightyellow")
add_frame("Frame 1 Content", "lightgreen")
add_frame("Frame 2 Content", "lightcoral")
add_frame("Frame 3 Content", "lightyellow")
add_frame("Frame 1 Content", "lightgreen")
add_frame("Frame 2 Content", "lightcoral")
add_frame("Frame 3 Content", "lightyellow")
add_frame("Frame 1 Content", "lightgreen")
add_frame("Frame 2 Content", "lightcoral")
add_frame("Frame 3 Content", "lightyellow")

# Start the Tkinter event loop
root.mainloop()