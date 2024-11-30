from tkinter import *
from tkinter import messagebox


root = Tk()

canvas_width = 800
canvas_height = 500

root.title("My GUI - Canvas")
root.geometry(f"{canvas_width}x{canvas_height}")
root.configure(bg="AliceBlue")  

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# the line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 500, fill="red")
can_widget.create_line(0, 500, 800, 0, fill="red")

# To create a rectangle specify parameters in this order - coors of top left and coors of bottom right
can_widget.create_rectangle(70, 70, 725, 425, fill="light blue")

can_widget.create_text(198, 193, text="Python")

can_widget.create_oval(314, 154, 477, 322, fill="orange")

root.mainloop()