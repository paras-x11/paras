from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("My GUI - Events")
root.geometry("600x500")

Label(root, text="double click to exit the program",borderwidth=5, bg="lightblue1", relief=FLAT).pack( pady=70)

btn = Button(root, text="CLick Me", bg="light blue") 
btn.pack(pady=20)

def location(event):
    print(f"You clicked the button at position {event.x}, {event.y}")

btn.bind('<Button-1>', location)
btn.bind('<Double-1>', quit)

root.mainloop()